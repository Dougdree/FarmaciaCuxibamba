from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from Cuxibamba import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', lambda request: redirect('register')),  # Redirige al registro por defecto
    path('menu/', views.menu_view, name='menu'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_medicamento/', views.crear_medicamento, name='crear_medicamento'),
    path('inventario/', views.inventario, name='inventario'),
    path('crear/', views.crear_factura, name='crear_factura'),
    path('ver/', views.ver_facturas, name='ver_facturas'),
    path('gestionar_transferencia/', views.gestionar_transferencia, name='gestionar_transferencia'),
    path('historial_transferencias/', views.historial_transferencias, name='historial_transferencias'),

]
