from django.db import models

class Farmacia(models.Model):
    numero_farmacia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre  # Ahora devuelve el nombre de la farmacia


class Sucursal(models.Model):
    num_sucursal = models.CharField(max_length=50)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    farmacia = models.ForeignKey(Farmacia, related_name='sucursal_list', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.num_sucursal} - {self.direccion}"  # Ahora devuelve el número de la sucursal y su dirección


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre  # Ahora devuelve el nombre de la categoría


class Medicamento(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='medicamento_list', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre  # Ahora devuelve el nombre del medicamento


class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, related_name='inventario_list', on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, related_name='inventario_list', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.medicamento.nombre} - {self.sucursal.num_sucursal}"  # Muestra medicamento y sucursal

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre  # Ahora devuelve el nombre de la persona


class Cliente(Persona):
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre  # Ahora devuelve el nombre del cliente


class Rol(models.TextChoices):
    ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'
    EMPLEADO = 'EMPLEADO', 'Empleado'


class Empleado(Persona):
    sucursal = models.ForeignKey(Sucursal, related_name='empleado_list', on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=Rol.choices)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"  # Muestra el nombre del empleado y su rol


class MetodoDePago(models.TextChoices):
    EFECTIVO = 'EFECTIVO', 'Efectivo'
    TARJETA = 'TARJETA', 'Tarjeta'
    TRANSFERENCIA = 'TRANSFERENCIA', 'Transferencia'


class Factura(models.Model):
    numero_factura = models.IntegerField()
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, related_name='factura_list', on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, related_name='factura_list', on_delete=models.CASCADE)
    total = models.FloatField()
    metodo_de_pago = models.CharField(max_length=20, choices=MetodoDePago.choices)

    def __str__(self):
        return f"Factura #{self.numero_factura} - {self.cliente.nombre}"  # Muestra el número de factura y el nombre del cliente


class ItemFactura(models.Model):
    numero_item_factura = models.IntegerField()
    factura = models.ForeignKey(Factura, related_name='item_factura_list', on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, related_name='item_factura_list', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

    def __str__(self):
        return f"Item #{self.numero_item_factura} - {self.medicamento.nombre}"  # Muestra el número del ítem y el nombre del medicamento


class Estado(models.TextChoices):
    PENDIENTE = 'PENDIENTE', 'Pendiente'
    COMPLETADA = 'COMPLETADA', 'Completada'
    CANCELADA = 'CANCELADA', 'Cancelada'


class Transferencia(models.Model):
    numero_transferencia = models.IntegerField()
    medicamento = models.ForeignKey(Medicamento, related_name='transferencia_list', on_delete=models.CASCADE)
    sucursal_origen = models.ForeignKey(Sucursal, related_name='transferencias_origen', on_delete=models.CASCADE)
    sucursal_destino = models.ForeignKey(Sucursal, related_name='transferencias_destino', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=Estado.choices)

    def __str__(self):
        return f"Transferencia #{self.numero_transferencia} - {self.medicamento.nombre}"  # Muestra el número de transferencia y el nombre del medicamento
