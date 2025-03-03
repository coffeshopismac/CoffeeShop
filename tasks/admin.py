from django.contrib import admin
<<<<<<< HEAD
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django.urls import path
from .models import Cliente, Categoria, Pedido, Producto, Empleado, Inventario, DetallePedido, Venta

# Personalización del panel de administración
class MyAdminSite(AdminSite):
    site_header = "Mi Administración"
    site_title = "Administración"
    index_title = "Bienvenido a la administración"

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('admin_custom.css', self.admin_view(self.custom_css)),
        ]
        return urls

    def custom_css(self, request):
        return HttpResponse('/* Aquí va tu CSS personalizado */', content_type='text/css')

admin_site = MyAdminSite(name='myadmin')

# Registro de modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Inventario)
admin.site.register(DetallePedido)
admin.site.register(Venta)
=======

# Register your models here.
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
