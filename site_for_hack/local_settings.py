import os.path
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p1&jpbk2tie^@tqbjp_$1e4%#fyg_n0odpntjp_(_nf_jj$aei'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'arh_map',
        'USER': 'map_user',
        'PASSWORD': 'mapper',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
