from django.urls import path
from . import views

app_name = 'wedding'
urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('detail/<int:mc_id>/', views.detail, name='detail'),
    path('list/', views.mc_list, name='mc_list'),
    path('cast/', views.cast, name='cast'),
    path('cast/success/', views.cast_success, name='cast_success'),
]
