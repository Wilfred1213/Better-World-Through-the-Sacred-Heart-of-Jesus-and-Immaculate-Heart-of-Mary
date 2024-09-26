
from django.urls import path, include
from . import views

app_name = 'homeApp'
urlpatterns = [
    path("", views.index, name="index"),
    path('sacrament/', views.sacrament, name='sacrament'),
    path('allsaints/', views.allsaints, name='allsaints'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
    path('sacramental_detail/<int:sac_id>/', views.sacramental_detail, name='sacramental_detail'),
    path('contact/', views.contact, name='contact'),
    path('saint_detail/<int:saint_id>/', views.saint_detail, name='saint_detail'),
    path('contact_messages/', views.contact_messages, name='contact_messages'),
    path('delete_contact/<int:message_id>/', views.delete_contact, name='delete_contact'),
    
]