# Generated by Django 5.1.4 on 2025-02-14 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleado_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('puesto', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usuario', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('impuestos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente')),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_producto', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('inventario_id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_disponible', models.IntegerField()),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('detalle_id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('venta_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.pedido')),
            ],
        ),
    ]
