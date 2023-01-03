from django.urls import path
from . import views

app_name = 'academy'
urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/', views.introduce, name='introduce'),
    path('course/', views.course, name='course'),
    path('notice/', views.notice, name='notice'),
    path('notice/<int:notice_id>/', views.notice_article, name='notice_article'),
    path('event/', views.event, name='event'),
    path('event/<int:event_id>/', views.event_article, name='event_article'),
    path('success/', views.success, name='success'),
    path('success/<int:success_id>/', views.success_article, name='success_article'),
    path('onlineform/', views.onlineform, name='_onlineform'),
    path('onlineform/success/', views.onlineform_success, name='onlineform_success')
]
