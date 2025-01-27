# APE.- Farmacias

## Datos Personales

**Nombre:** Douglas Andrey Carreño Pardo  
**Carrera:** Segundo Ciclo de Ingeniería en Ciencias de la Computación  


## Descripción del Problema
El proyecto APE.- Farmacias consiste en desarrollar un sistema de gestión para una cadena de farmacias con múltiples sucursales. El objetivo principal del sistema es permitir la venta de medicamentos en una sucursal determinada. En caso de que un producto no esté disponible en la sucursal solicitada, el sistema debe permitir la venta del medicamento desde otra sucursal, con la opción de que el cliente pueda retirarlo en la sucursal de origen o recibirlo directamente en la sucursal donde realizó la compra.

El sistema se desarrollará utilizando el framework Django, permitiendo la gestión de inventarios, ventas, transferencias entre sucursales y seguimiento de pedidos.

## Objetivos del Sistema

- **Gestión de Inventario:** Controlar el stock de medicamentos en cada sucursal.
- **Venta de Medicamentos:** Permitir la venta de productos disponibles en la sucursal.
- **Transferencias entre Sucursales:** Habilitar la compra de medicamentos desde otra sucursal en caso de falta de stock local.
- **Opciones de Entrega:** Ofrecer la opción de retirar el medicamento en la sucursal o enviarlo a la sucursal de origen.
- **Registro de Clientes y Pedidos:** Gestionar clientes, pedidos y seguimiento de entrega.
- **Autenticación de Usuarios:** Roles para administrador, empleado de sucursal y cliente.

## Diagrama de Clases

![Diagrama de Clases](https://github.com/user-attachments/assets/05ac9178-c2a8-45b1-ae8f-da42d728a5cd)

## Dirección de Código del Proyecto
-**Aplicaciones Principales**
- [models.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/models.py)
- [admin.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/admin.py)
- [views.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/views.py)
- [forms.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/forms.py)
- [urls.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Farmacia/urls.py)
- **Dirección de los Templates**
- [register.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/register.html)
- [login.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/login.html)
- [crear_categoría.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/crear_categoria.html)
- [crear_factura.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/crear_factura.html)
- [crear_medicamento.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/crear_medicamento.html)
- [gestión_transferencia.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/gestion_transferencia.html)
- [historial_transferencia.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/historial_transferencias.html)
- [inventario.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/inventario.html)
- [menú_principal.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/menu_principal.html)
- [styless.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/styles.css)
- [ver_facturas.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/templates/ver_facturas.html)
