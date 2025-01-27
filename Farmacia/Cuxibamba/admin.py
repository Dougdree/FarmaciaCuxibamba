from django.contrib import admin
from .models import (
    Farmacia, Sucursal, Categoria, Medicamento, Inventario,
    Cliente, Empleado, Factura, ItemFactura, Transferencia
)

class ItemFacturaInline(admin.TabularInline):
    model = ItemFactura
    extra = 1  # Número de filas extra

@admin.register(Farmacia)
class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('numero_farmacia', 'nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'numero_farmacia')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('num_sucursal', 'direccion', 'telefono', 'farmacia')
    search_fields = ('num_sucursal', 'direccion')
    list_filter = ('farmacia',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'medicamento', 'cantidad')
    list_filter = ('sucursal', 'medicamento')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'telefono', 'email')
    search_fields = ('nombre', 'cedula', 'email')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'sucursal', 'rol')
    search_fields = ('nombre', 'cedula')
    list_filter = ('rol', 'sucursal')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'fecha', 'cliente', 'sucursal', 'total', 'metodo_de_pago')
    search_fields = ('numero_factura', 'clientenombre')
    list_filter = ('fecha', 'metodo_de_pago', 'sucursal')
    inlines = [ItemFacturaInline]

@admin.register(ItemFactura)
class ItemFacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_item_factura', 'factura', 'medicamento', 'cantidad', 'subtotal')
    list_filter = ('factura', 'medicamento')

@admin.register(Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_transferencia', 'medicamento', 'sucursal_origen', 'sucursal_destino', 'cantidad', 'fecha', 'estado')
    search_fields = ('numero_transferencia', 'medicamentonombre')
    list_filter = ('fecha', 'estado', 'sucursal_origen', 'sucursal_destino')