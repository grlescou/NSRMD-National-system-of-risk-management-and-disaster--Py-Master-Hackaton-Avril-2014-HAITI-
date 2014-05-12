"""
Django settings for geoDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2=9ayr(=$%gwdil=-5%9^xq)mxinkli-im_&d5jo8ua-yq%zfa'

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
    'django.contrib.gis',
    'gestionR',
    'geoDjango',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'geoDjango.urls'

WSGI_APPLICATION = 'geoDjango.wsgi.application'

FTP_STORAGE_LOCATION = 'ftp://<jocrash>:<jesuspa$$word>@<ftp.alwaysdata.com>:<21>/media/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'PostGIS',  # Name of your spatial database
#         'USER': 'postgres',   # Database user
#         'PASSWORD': 'password',# Database password
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
#
#
# GEOS_LIBRARY_PATH = '/app/.geodjango/geos/lib/libgeos_c.so'
#
# GDAL_LIBRARY_PATH = '/app/.geodjango/gdal/lib/libgdal.so'



DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'grl_geodjango',
        'USER': 'grl',
        'PASSWORD': '!!GAROLE!!90$$',
        'PORT': '5432',
        'HOST': 'postgresql1.alwaysdata.com',
    }
}


#GDAL_LIBRARY_PATH = 'C:/lastgeodjango/gdal/gdal110.dll'
#GEOS_LIBRARY_PATH = 'C:/lastgeodjango/geos/bin/geos_c.dll'

##Heroku setting for dll
GEOS_LIBRARY_PATH = '/app/.geodjango/geos/lib/libgeos_c.so'
#
GDAL_LIBRARY_PATH = '/app/.geodjango/gdal/lib/libgdal.so'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    "geoDjango/templates/static",
)


import dj_database_url
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
# # Allow all host headers
ALLOWED_HOSTS = ['*']

#Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    "geoDjango/templates/static",
)


MEDIA_ROOT = os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'templates'),'static'),'media\\').replace('\\','/')
MEDIA_URL = '/media/'

FTP_STORAGE_LOCATION = 'ftp://<jocrash>:<jesuspa$$word>@<ftp.alwaysdata.com>:<21>/media/'

print "root : "+MEDIA_ROOT
