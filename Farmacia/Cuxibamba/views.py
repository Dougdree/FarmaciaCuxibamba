from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Farmacia, Categoria, Cliente, Empleado
from .forms import InventarioForm
from .models import Factura
from .forms import FacturaForm, ItemFacturaForm
from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from .models import Sucursal, Medicamento, Inventario, Transferencia, Estado
from .forms import TransferenciaForm
import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CategoriaForm, MedicamentoForm


# Vista para el login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')  # Redirigir al menú después de iniciar sesión
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista para el registro
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda al usuario
            messages.success(request, '¡Te has registrado correctamente! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después del registro
        else:
            messages.error(request, 'Por favor, revisa los errores.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

# Vista para el menú
@login_required
def menu_view(request):
    # Obtenemos los objetos de tus modelos
    farmacias = Farmacia.objects.all()
    sucursales = Sucursal.objects.all()
    categorias = Categoria.objects.all()
    medicamentos = Medicamento.objects.all()
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()

    context = {
        'farmacias': farmacias,
        'sucursales': sucursales,
        'categorias': categorias,
        'medicamentos': medicamentos,
        'clientes': clientes,
        'empleados': empleados,
    }



    return render(request, 'menu_principal.html', context)

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')  # Redirige a la misma página o a otra vista
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})


def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirige a la página del menú principal después de crear
    else:
        form = MedicamentoForm()

    return render(request, 'crear_medicamento.html', {'form': form})


def inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')  # Redirige a la misma página para mostrar el inventario actualizado
    else:
        form = InventarioForm()

    inventarios = Inventario.objects.all()  # Obtiene todos los inventarios existentes
    return render(request, 'inventario.html', {'form': form, 'inventarios': inventarios})

def crear_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        item_factura_form = ItemFacturaForm(request.POST)

        if factura_form.is_valid() and item_factura_form.is_valid():
            with transaction.atomic():
                # Guardar la factura
                factura = factura_form.save()

                # Guardar los ítems de la factura
                medicamento = item_factura_form.cleaned_data['medicamento']
                cantidad = item_factura_form.cleaned_data['cantidad']
                subtotal = medicamento.precio * cantidad

                item_factura = item_factura_form.save(commit=False)
                item_factura.factura = factura
                item_factura.subtotal = subtotal
                item_factura.save()

                # Calcular el total de la factura
                factura.total = sum([item.subtotal for item in factura.item_factura_list.all()])
                factura.save()

            return redirect('ver_facturas')
    else:
        factura_form = FacturaForm()
        item_factura_form = ItemFacturaForm()

    return render(request, 'crear_factura.html', {'factura_form': factura_form, 'item_factura_form': item_factura_form})

def ver_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'ver_facturas.html', {'facturas': facturas})


def gestionar_transferencia(request):
    if request.method == 'POST':
        form = TransferenciaForm(request.POST)
        if form.is_valid():
            medicamento = form.cleaned_data['medicamento']
            sucursal_origen = form.cleaned_data['sucursal_origen']
            sucursal_destino = form.cleaned_data['sucursal_destino']
            cantidad = form.cleaned_data['cantidad']

            # Llamamos a la función de gestionar la transferencia
            return gestionar_transferencia_logica(medicamento, sucursal_origen, sucursal_destino, cantidad)
    else:
        form = TransferenciaForm()

    return render(request, 'gestion_transferencia.html', {'form': form})


def gestionar_transferencia_logica(medicamento, sucursal_origen, sucursal_destino, cantidad):
    # Verificar si la sucursal de origen tiene suficiente inventario
    inventario_origen = Inventario.objects.filter(sucursal=sucursal_origen, medicamento=medicamento).first()

    if not inventario_origen or inventario_origen.cantidad < cantidad:
        # Si no tiene suficiente stock, intentamos buscar en otras sucursales
        otras_sucursales = Sucursal.objects.exclude(id=sucursal_origen.id)
        for sucursal in otras_sucursales:
            inventario = Inventario.objects.filter(sucursal=sucursal, medicamento=medicamento).first()
            if inventario and inventario.cantidad >= cantidad:
                # Realizar la transferencia
                return realizar_transferencia(medicamento, sucursal, sucursal_destino, cantidad)

        # Si no hay suficiente stock en otras sucursales, tratamos de realizar la transferencia desde la misma sucursal
        if inventario_origen and inventario_origen.cantidad >= cantidad:
            return realizar_transferencia(medicamento, sucursal_origen, sucursal_destino, cantidad)
        else:
            return HttpResponse("No hay suficiente stock disponible en las sucursales para realizar la transferencia.",
                                status=400)
    else:
        # Si tiene suficiente stock en la misma sucursal, se realiza la transferencia
        return realizar_transferencia(medicamento, sucursal_origen, sucursal_destino, cantidad)


def realizar_transferencia(medicamento, sucursal_origen, sucursal_destino, cantidad):
    with transaction.atomic():
        # Reducir el inventario de la sucursal de origen
        inventario_origen = Inventario.objects.get(sucursal=sucursal_origen, medicamento=medicamento)
        inventario_origen.cantidad -= cantidad
        inventario_origen.save()

        # Aumentar el inventario de la sucursal de destino
        inventario_destino, created = Inventario.objects.get_or_create(sucursal=sucursal_destino,
                                                                       medicamento=medicamento)
        inventario_destino.cantidad += cantidad
        inventario_destino.save()

        # Crear un registro de transferencia
        transferencia = Transferencia.objects.create(
            medicamento=medicamento,
            sucursal_origen=sucursal_origen,
            sucursal_destino=sucursal_destino,
            cantidad=cantidad,
            fecha=datetime.date.today(),
            estado=Estado.PENDIENTE
        )

        return HttpResponse(f"Transferencia de {cantidad} unidades de {medicamento.nombre} realizada con éxito.")

def historial_transferencias(request):
    # Obtener todas las transferencias
    transferencias = Transferencia.objects.all().order_by('-fecha')  # Ordenamos por la fecha de manera descendente
    return render(request, 'historial_transferencias.html', {'transferencias': transferencias})

def custom_logout(request):
    logout(request)
    return redirect('login')
