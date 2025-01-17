"""
Django settings for buecherboerse project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x5e(9g4uyg%6fel^fp-xyq!yi+3e_e%+s)y@o3a&okug=5v5mj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost","127.0.0.1","dev.leandergoetz.eu","blog.leandergoetz.eu","leandergoetz.eu"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'search',
    'drf_yasg',
    'rest_framework',
    'django_filters',
]

MIDDLEWARE = [
    'search.middleware.JWTAuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 20
}


ROOT_URLCONF = 'buecherboerse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'buecherboerse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'ATOMIC_REQUESTS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

CORS_ALLOWED_ORIGINS = [
    "https://nuxt-auth-new.vercel.app",
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'de-at'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=100),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True


import os

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Set the base directory of your project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the templates directory
# settings.py

# Define the path to the templates directory
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
# DRF-YASG configuration
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    #'USE_SESSION_AUTH': True,  # To disable Django session authentication
    #'PERSIST_AUTH': True,  # To persist authentication credentials across sessions
    'LOGIN_URL': '/api/v1/auth/login',
    #'LOGOUT_URL': 'rest_framework:auth_logout',
    #'DOC_EXPANSION': 'list',
    #'YASG_JS': 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.52.1/swagger-ui-bundle.js',
    #'YASG_CSS': 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.52.1/swagger-ui.css',
    #'YASG_TEMPLATE': os.path.join(TEMPLATES_DIR, 'swagger_ui_custom.html'),  # Path to your custom template
}

CSRF_TRUSTED_ORIGINS = ['https://blog.leandergoetz.eu','https://dev.leandergoetz.eu']
SESSION_COOKIE_DOMAIN = '.leandergoetz.eu'
CSRF_COOKIE_DOMAIN = '.leandergoetz.eu'
