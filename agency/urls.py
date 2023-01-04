from django.urls import path
from . import views

app_name = 'agency'
urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/', views.introduce, name='introduce'),
    path('list/', views.mc_list, name='mc_list'),
    path('detail/<int:announcer_id>/', views.detail, name='detail'),
    path('onlineform/', views.onlineform, name='onlineform'),
    path('onlineform/success/', views.onlineform_success, name='onlineform_success'),
    path('event/', views.event, name='event')
]