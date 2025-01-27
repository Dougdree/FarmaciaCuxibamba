from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Medicamento, Categoria
from .models import Inventario
from .models import Factura, ItemFactura, Cliente, Sucursal


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario registrado con este correo.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}),
        label="Nombre de Usuario"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}),
        label="Contraseña"
    )

    class Meta:
        fields = ['username', 'password']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la categoría'}),
        }

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'precio', 'descripcion', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del medicamento'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }



class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['sucursal', 'medicamento', 'cantidad']


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['numero_factura', 'fecha', 'cliente', 'sucursal', 'metodo_de_pago']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), label="Cliente")
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all(), label="Sucursal")
    metodo_de_pago = forms.ChoiceField(choices=Factura._meta.get_field('metodo_de_pago').choices,
                                       label="Método de Pago")
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'}))



class ItemFacturaForm(forms.ModelForm):
    class Meta:
        model = ItemFactura
        fields = ['medicamento', 'cantidad', 'subtotal']

    medicamento = forms.ModelChoiceField(queryset=Medicamento.objects.all(), label="Medicamento")
    cantidad = forms.IntegerField(min_value=1, label="Cantidad")
    subtotal = forms.FloatField(label="Subtotal", required=False)

class TransferenciaForm(forms.Form):
    medicamento = forms.ModelChoiceField(queryset=Medicamento.objects.all(), label="Medicamento", widget=forms.Select(attrs={'class': 'form-control'}))
    sucursal_origen = forms.ModelChoiceField(queryset=Sucursal.objects.all(), label="Sucursal Origen", widget=forms.Select(attrs={'class': 'form-control'}))
    sucursal_destino = forms.ModelChoiceField(queryset=Sucursal.objects.all(), label="Sucursal Destino", widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(label="Cantidad", min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))




