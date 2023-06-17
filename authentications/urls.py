from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'authentications'

urlpatterns =[
    path('signup/', views.signup, name='signup'),
    path('loggin/', views.loggin, name='loggin'),
    path('logout/', views.logout, name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),
    # path('newsletter/', views.newsletter, name='newsletter'),
    #path('accounts/', include("django.contrib.auth.urls")),
    
    
    
]