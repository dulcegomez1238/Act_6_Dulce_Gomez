from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Producto, Inventario

# Página de inicio
def inicio_Farmacia(request):
    return render(request, "inicio.html")

# Agregar proveedor
def agregar_proveedor(request):
    if request.method == "POST":
        Proveedor.objects.create(
            nombre=request.POST["nombre"],
            direccion=request.POST["direccion"],
            telefono=request.POST["telefono"],
            correo_electronico=request.POST["correo_electronico"],
            tipo_producto=request.POST["tipo_producto"],
        )
        return redirect("ver_proveedor")
    return render(request, "proveedor/agregar_proveedor.html")

# Ver proveedores
def ver_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, "proveedor/ver_proveedor.html", {"proveedores": proveedores})

# Actualizar proveedor
def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, "proveedor/actualizar_proveedor.html", {"proveedor": proveedor})

# Realizar actualización
def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.nombre = request.POST["nombre"]
    proveedor.direccion = request.POST["direccion"]
    proveedor.telefono = request.POST["telefono"]
    proveedor.correo_electronico = request.POST["correo_electronico"]
    proveedor.tipo_producto = request.POST["tipo_producto"]
    proveedor.save()
    return redirect("ver_proveedor")

# Borrar proveedor
def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect("ver_proveedor")



# ----- PRODUCTO -----

def agregar_producto(request):
    proveedores = Proveedor.objects.all()

    if request.method == "POST":
        Producto.objects.create(
            nombre=request.POST["nombre"],
            tipo_producto=request.POST["tipo_producto"],
            fecha_caducidad=request.POST["fecha_caducidad"],
            precio=request.POST["precio"],
            proveedor_id=request.POST["proveedor"]
        )
        return redirect("ver_producto")

    return render(request, "producto/agregar_producto.html", {"proveedores": proveedores})


def ver_producto(request):
    productos = Producto.objects.all()
    return render(request, "producto/ver_producto.html", {"productos": productos})


def actualizar_producto(request, id):
    producto = Producto.objects.get(id=id)
    proveedores = Proveedor.objects.all()
    return render(request, "producto/actualizar_producto.html", {"producto": producto, "proveedores": proveedores})


def realizar_actualizacion_producto(request, id):
    producto = Producto.objects.get(id=id)

    producto.nombre = request.POST["nombre"]
    producto.tipo_producto = request.POST["tipo_producto"]
    producto.fecha_caducidad = request.POST["fecha_caducidad"]
    producto.precio = request.POST["precio"]
    producto.proveedor_id = request.POST["proveedor"]
    producto.save()

    return redirect("ver_producto")


def borrar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect("ver_producto")


# ----- INVENTARIO -----

def agregar_inventario(request):
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == "POST":
        Inventario.objects.create(
            producto_id=request.POST["producto"],
            nombre=request.POST["nombre"],
            tipo=request.POST["tipo"],
            fecha_caducidad=request.POST["fecha_caducidad"],
            proveedor_id=request.POST["proveedor"],
            contenido=request.POST["contenido"]
        )
        return redirect("ver_inventario")

    return render(request, "inventario/agregar_inventario.html",
                  {"productos": productos, "proveedores": proveedores})


def ver_inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, "inventario/ver_inventario.html", {"inventarios": inventarios})


def actualizar_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()

    return render(request, "inventario/actualizar_inventario.html",
                  {"inventario": inventario, "productos": productos, "proveedores": proveedores})


def realizar_actualizacion_inventario(request, id):
    inventario = Inventario.objects.get(id=id)

    inventario.producto_id = request.POST["producto"]
    inventario.nombre = request.POST["nombre"]
    inventario.tipo = request.POST["tipo"]
    inventario.fecha_caducidad = request.POST["fecha_caducidad"]
    inventario.proveedor_id = request.POST["proveedor"]
    inventario.contenido = request.POST["contenido"]
    inventario.save()

    return redirect("ver_inventario")


def borrar_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    inventario.delete()

    return redirect("ver_inventario")
