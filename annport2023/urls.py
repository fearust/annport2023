from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common import views

# https://github.com/jazzband/django-hosts
# https://docs.djangoproject.com/en/2.1/ref/contrib/sites/
# https://www.reddit.com/r/django/comments/99n110/django_subdomain_per_app/
# subdomain per app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wedding/', include('wedding.urls')),
    path('academy/', include('academy.urls')),
    path('agency/', include('agency.urls')),
    path('', views.index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
