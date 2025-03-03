<<<<<<< HEAD
=======
"""
Django settings for django_crud_api project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
<<<<<<< HEAD
BASE_DIR = Path(__file__).resolve().parent.parent  # Mantén esta línea
=======
BASE_DIR = Path(__file__).resolve().parent.parent

>>>>>>> a1208405d428e12e418b775e30138426a17d67f5

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5_!&pjim$p47f!pmq)@j4ja7(!2mib1_(%4v5^xq-$=e6+8_zb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

<<<<<<< HEAD
=======

>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'whitenoise.runserver_nostatic',
=======
     'whitenoise.runserver_nostatic',
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
    'corsheaders',
    'rest_framework',
    'coreapi',
    'tasks'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'django_crud_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [os.path.join(BASE_DIR, "django_crud_api", 'templates')],  # Esto ahora funcionará correctamente
=======
        'DIRS': [],
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_crud_api.wsgi.application'

<<<<<<< HEAD
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Motor de MySQL
        'NAME': 'dbcafeteria', 
        'USER': 'root',  
        'PASSWORD': 'root',  
        'HOST': 'localhost',  # Servidor de MySQL 
        'PORT': '3306',  # Puerto de MySQL (por defecto es 3306)
    }
}

# Password validation
=======

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    "default":
    dj_database_url.config(default="sqlite:///" +
                           os.path.join(BASE_DIR, "db.sqlite3"))
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

<<<<<<< HEAD
# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS authorization
=======

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
  # Tell Django where to look for React's static files (css, js)
  os.path.join(BASE_DIR, "client", "dist")
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#cors autorizacion
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
<<<<<<< HEAD
}

# Static files directories
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
LOGIN_REDIRECT_URL = '/admin/'
=======
    
}
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
