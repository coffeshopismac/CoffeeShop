<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    TaskSerializer, ClienteSerializer, CategoriaSerializer, ProductoSerializer,
    EmpleadoSerializer, PedidoSerializer, DetallePedidoSerializer, InventarioSerializer, VentaSerializer
)
from .models import Task, Cliente, Categoria, Producto, Empleado, Pedido, DetallePedido, Inventario, Venta

# Vista para la página de información de la empresa
def info_empresa(request):
    return render(request, 'info_empresa.html')

# Vistas de la API REST
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
=======
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
