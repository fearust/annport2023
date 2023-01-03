from .base import *
import environ

DEBUG = False

ALLOWED_HOSTS = ['3.35.114.141']

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}

# Static, media
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/annport2023/static'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_files'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ubuntu/annport2023/media'

DATA_UPLOAD_MAX_MEMORY_SIZE = 100*1024*1024
