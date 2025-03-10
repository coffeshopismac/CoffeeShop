"""django_crud_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings
<<<<<<< HEAD
from django.contrib.auth import views as auth_views

=======
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tasks.urls')),  # Cambié esta línea para que esté bajo 'api/v1/'
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
<<<<<<< HEAD
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
=======
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)