"""
Django settings for sasoficial project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


with open('sasoficial/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()



# SECRET_KEY = 'django-insecure-w0w=t@2(#-i*$z0%uid^wi=%e*an=#*qla3c%6!#iapoh+2@%9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

# ALLOWED_HOSTS = ['*', 'localhost', '0.0.0.0']
# ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = ['sasoficialia.villahermosa.gob.mx', '.sasoficialia.villahermosa.gob.mx','localhost']



APPEND_SLASH = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'home.apps.HomeConfig',
    'proyecto.apps.ProyectoConfig',
    'oficiosenviados.apps.OficiosenviadosConfig',
    'crispy_forms',
    'widget_tweaks'
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 'siad___.Middleware.TimezoneMiddleware.TimezoneMiddleware',
# 'whitenoise.middleware.WhiteNoiseMiddleware'

ROOT_URLCONF = 'sasoficial.urls'

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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 30000
    }
}

AUTH_USER_MODEL = "home.Usuario"

WSGI_APPLICATION = 'sasoficial.wsgi.application'
# WSGI_APPLICATION = 'wsgi.application'

CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "http://"

SECURE_HSTS_SECONDS = 31536000
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = True
SECURE_FRAME_DENY = False

# CSRF_TRUSTED_ORIGINS = ['https://sasoficialia.villahermosa.gob.mx','https://.sasoficialia.villahermosa.gob.mx','https://127.0.0.1']



# import os
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ['https://sasoficialia.villahermosa.gob.mx','https://.sasoficialia.villahermosa.gob.mx','https://127.0.0.1']



# if os.environ.get('DJANGO_ENV') is not None:
#     SECURE_SSL_REDIRECT = False
#     SESSION_COOKIE_SECURE = False
#     CSRF_COOKIE_SECURE = False
# else:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1025853736279-0novh6onovnogu4f829nrhpd8hlko8gl.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbsasoficialia',
        'USER': 'postgres',
        'PASSWORD': 'R=D7,Z)$F%q,Kj?CP,DM{1CFNTtQ1B@4=V!d',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-Mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True
USE_L10N = True
USE_TZ = True

JQUERY_URL = True

USE_DJANGO_JQUERY = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/home/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATE_FORMAT = '%Y-%m-%d'
DATE_INPUT_FORMATS = ['%Y-%m-%d']

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S']

# DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'
# DATETIME_INPUT_FORMATS = ['%d-%m-%Y %H:%M:%S']

STATIC_URL = 'static/'
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REPORTS_URL = '/media/reports/'
REPORTS_ROOT = os.path.join(BASE_DIR, 'media/reports')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ITEMS_FOR_PAGE = 25

URL_OFICIO = 'oficios_search_data_list'
URL_OFICIO_ENVIADO = 'oficiosenviados_search_data_list'
