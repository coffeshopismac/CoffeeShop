from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views
from .views import (
    ClienteViewSet, CategoriaViewSet, ProductoViewSet, EmpleadoViewSet,
    PedidoViewSet, DetallePedidoViewSet, InventarioViewSet, VentaViewSet,
    info_empresa
)

# Configurar el router para las API REST
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')
router.register(r'clientes', ClienteViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detallepedidos', DetallePedidoViewSet)
router.register(r'inventarios', InventarioViewSet)
router.register(r'ventas', VentaViewSet)

# Lista final de URLs
urlpatterns = [
    path("", include(router.urls)),  # API REST
    path("api/", include(router.urls)),  
    path("docs/", include_docs_urls(title="Tasks API")),  # Documentación de la API
    path('info_empresa/', info_empresa, name='info_empresa'),  # Página de información de la empresa
    
]
