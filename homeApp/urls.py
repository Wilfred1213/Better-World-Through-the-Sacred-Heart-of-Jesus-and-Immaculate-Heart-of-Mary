
from django.urls import path, include
from . import views

app_name = 'homeApp'
urlpatterns = [
    path("", views.index, name="index"),
    path('focolare/', views.focolare, name='focolare'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
    path('focolare_detail/<int:foco_id>/', views.focolare_detail, name='focolare_detail')
    
]