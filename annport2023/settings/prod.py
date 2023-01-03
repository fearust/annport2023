from .base import *

DEBUG = False

ALLOWED_HOSTS = ['3.35.114.141']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Static, media
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/annport2023/static'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_files'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ubuntu/annport2023/media'

DATA_UPLOAD_MAX_MEMORY_SIZE = 100*1024*1024
