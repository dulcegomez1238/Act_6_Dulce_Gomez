from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Farmacia, name="inicio"),
    path('agregar_proveedor/', views.agregar_proveedor, name="agregar_proveedor"),
    path('ver_proveedor/', views.ver_proveedor, name="ver_proveedor"),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name="actualizar_proveedor"),
    path('realizar_actualizacion_proveedor/<int:id>/', views.realizar_actualizacion_proveedor),
    path('borrar_proveedor/<int:id>/', views.borrar_proveedor),

        # PRODUCTOS
    path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
    path('ver_producto/', views.ver_producto, name="ver_producto"),
    path('actualizar_producto/<int:id>/', views.actualizar_producto, name="actualizar_producto"),
    path('realizar_actualizacion_producto/<int:id>/', views.realizar_actualizacion_producto),
    path('borrar_producto/<int:id>/', views.borrar_producto),

    # INVENTARIO
    path('agregar_inventario/', views.agregar_inventario, name="agregar_inventario"),
    path('ver_inventario/', views.ver_inventario, name="ver_inventario"),
    path('actualizar_inventario/<int:id>/', views.actualizar_inventario, name="actualizar_inventario"),
    path('realizar_actualizacion_inventario/<int:id>/', views.realizar_actualizacion_inventario),
    path('borrar_inventario/<int:id>/', views.borrar_inventario),

]
