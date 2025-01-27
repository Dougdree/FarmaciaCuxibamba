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
**Aplicaciones Principales**
- [models.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/models.py)
- [admin.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/admin.py)
- [views.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/views.py)
- [forms.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Cuxibamba/forms.py)
- [urls.](https://github.com/Dougdree/FarmaciaCuxibamba/blob/develop/Farmacia/Farmacia/urls.py)

  
**Dirección de los Templates**
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

**Capturas de la Interfaz del Programa**
![image](https://github.com/user-attachments/assets/55008081-f92b-4a2f-9a7e-318667122b25)
La interfaz que se muestra en la Figura 1 es donde al ejecutar el programa te redirecciona automáticamente el cual es el register para poder tener una cuenta para el uso del programa.

![image](https://github.com/user-attachments/assets/f105a3dc-4b74-49f7-9ee0-70ab9aaa5406)
La interfaz que se muestra en la Figura 2 es donde se direcciona luego de registrar una cuenta en el programa.

![image](https://github.com/user-attachments/assets/a6a35a59-e949-43ce-a806-0340f8ef8da1)
La interfaz que se muestra en la Figura 3 es donde se direcciona luego de logearte en el programa, cómo se puede observar tiene un pequeño menú con algunas funciones que ya iré presentando.

![image](https://github.com/user-attachments/assets/01173ae8-0861-4eba-839b-bd326b026e82)
La interfaz que se muestra en la Figura 4 es donde se direciona al darle click en "Crear Medicamento", cómo se puede observar nos permite ingresar nombre, precio, descripción y categoría. Además de contar con el botón de regresar al menú.

![image](https://github.com/user-attachments/assets/de8b2727-e381-48a3-9fa7-7caa51ae845b)
La interfaz que se muestra en la Figura 5 es donde se direcciona al darle click en "Inventario", cómo se puede observar nos permite ingresar surcursal, medicamento, cantidad y nos permite visualizar el inventario existente.

![image](https://github.com/user-attachments/assets/a8b4b7ef-15ea-477d-a189-59f9a4560156)
La interfaz que se muestra en la Figura 6 es donde se direcciona al darle click en "Crear Factura", cómo se puede observar nos permite añadir un cliente, surcursal, fecha, total, método de pago y además en la parte inferior tenemos el item de Factura para mejor accesibilidad.

![image](https://github.com/user-attachments/assets/0734e4fd-a033-4b84-b7a3-092d8c19d2b6)
La interfaz que se muestra en la figura 7 es donde se direcciona al darle click en "Ver facturas", cómo se puede observar nos permite visualizar las facturas creadas anteriormente.

![image](https://github.com/user-attachments/assets/228479be-d4bd-42de-bce0-3cb52794ea38)
La interfaz que se muestra en la figura 8 es donde se direcciona al darle click en "Gestionar Transferencia", cómo se puede observar nos permite añadir el medicamento, surcursal de origen y surcursal del destino, la cantidad del medicamento y el estado de la transferencia.

![image](https://github.com/user-attachments/assets/d07d86b8-2ee7-4c96-802f-a76334be61d4)
La interfaz que se muestra en la figura 9 es donde se direcciona al darle click en "Historial de Transferencias", cómo se puede observar nos permite visualizar las transferencias, con susurcursal de origen y destino, además de la cantidad, la fecha y el estado.

![image](https://github.com/user-attachments/assets/d45c136e-df5f-47bb-b565-64e4364acfc1)
La interfaz que se muestra en la figura 10 es donde se direcciona al darle click en "Crear Categoria", ahí se puede crear una categoría de los medicamentos, por ejemplo las vitaminas.








