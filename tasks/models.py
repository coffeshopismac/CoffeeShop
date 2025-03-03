from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
<<<<<<< HEAD
        return self.title
    
# Modelo Cliente
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    email = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo Categoria
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo Producto
class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    codigo_producto = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo Empleado
class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, null=True, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.pedido_id}"

# Modelo DetallePedido
class DetallePedido(models.Model):
    detalle_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.detalle_id}"

# Modelo Inventario
class Inventario(models.Model):
    inventario_id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Inventario {self.inventario_id}"

# Modelo Venta
class Venta(models.Model):
    venta_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.venta_id}"
=======
        return self.title
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
