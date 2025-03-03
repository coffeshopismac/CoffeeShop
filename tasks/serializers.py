from rest_framework import serializers
<<<<<<< HEAD
from .models import Task, Cliente, Categoria, Producto, Empleado, Pedido, DetallePedido, Inventario, Venta
=======
from .models import Task
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'title', 'description', 'done')
<<<<<<< HEAD
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()  # Para mostrar detalles de la categoría

    class Meta:
        model = Producto
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    empleado = EmpleadoSerializer()

    class Meta:
        model = Pedido
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()
    producto = ProductoSerializer()

    class Meta:
        model = DetallePedido
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = Inventario
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()

    class Meta:
        model = Venta
        fields = '__all__'        

=======
        fields = '__all__'
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
