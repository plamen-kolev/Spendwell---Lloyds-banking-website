# Code written by Plamen Kolev


"""
Django settings for Bank project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
)

heroku = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u)%as+uzv6!3#4fdy@7^&3l066ns8@t!p!4vmal#ef1k!(b14*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payment',
    'generator',
    'notification',
    'userprofile',
    'content_controller',
    'api',
    'budget',
    'help',

    'autofixture',
    'rest_framework',
    'rest_framework.authtoken',
    'tinymce',
    'colorful',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Bank.urls'

WSGI_APPLICATION = 'Bank.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if heroku:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ds990h4gm5icj',
            'USER': 'gdqnhlmmewjnxy',
            'PASSWORD': 'quGNzUdoDha65KesxUvyVEVvA-',
            'HOST': 'ec2-54-197-237-120.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static/'),
)

STATIC_ROOT = os.path.join(BASE_DIR,'static/production/')

MEDIA_ROOT = os.path.join(BASE_DIR, "static/media/")

MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = '/login'

LOGIN_URL = '/login'


#  rest rest_framework

REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': (
                'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
                'rest_framework.permissions.IsAuthenticated'
        ),
# from the api token authentication manual https://getblimp.github.io/django-rest-framework-jwt/#installation
        'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework.authentication.SessionAuthentication',
                'rest_framework.authentication.BasicAuthentication',
                'rest_framework.authentication.TokenAuthentication',
        ),
}