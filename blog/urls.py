from django.urls import path
from . import views

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,  PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('home/', views.home, name='home'),
    path('dailyprayer/', views.dailyprayer, name='dailyprayer'),
    path('prayer_details<int:id>/', views.prayer_details, name='prayer_details'),
    path('blog_details<int:id>/', views.blog_details, name='blog_details'),
    path('novena_details<int:id>/', views.novena_details, name='novena_details'),
    path('all_prayers/', views.all_prayers, name='all_prayers'),
    path('all_novena/', views.all_novena, name='all_novena'),
    path('all_stations_cross/', views.all_stations_cross, name='all_stations_cross'),
    path('station_details/<str:station_id>/', views.station_details, name='station_details'),
    path('opening_prayer/', views.opening_prayer, name='opening_prayer'),
    path('closing_prayer/', views.closing_prayer, name='closing_prayer'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('create_novena/', views.create_novena, name='create_novena'),
    path('create_days_of_novena/', views.create_days_of_novena, name='create_days_of_novena'),
        
    path('blog_post/', views.blog_post, name='blog_post'),
    path('liked_post/<int:id>', views.liked_post, name='liked_post'),
    path('liked_main_blog/', views.liked_main_blog, name='liked_main_blog'),
    path('message/<int:id>', views.message, name='message'),
    
    path('galary/', views.galary, name='galary'),
    path('aboutView/', views.aboutview, name='aboutView'),
    path('novenaView/', views.novenaView.as_view(), name='novenaView'),
    path('dailypassword/', views.dailypassword, name='dailypassword'),  
    path('deleteBlog/<int:id>/', views.deleteBlog, name='deleteBlog'),    
    path('dashbord/', views.dashbord, name='dashbord'),
    path('deleteComent/<int:blog_id>/', views.deleteComent, name="deleteComent"),
    path('deleteNovenaComent/<int:novena_id>/', views.deleteNovenaComent, name="deleteNovenaComent"),
    
    path('unsubscribe/', views.unsubscribe, name="unsubscribe"),
    path('unsub_confirmation/', views.unsub_confirmation, name="unsub_confirmation"),

    # change password
    path('change-password/', PasswordChangeView.as_view(
        template_name ='blog/auth/change-password.html'),   
        name='change-password'),
    path('change_password_done/', PasswordChangeDoneView.as_view(
        template_name ='blog/auth/password_change_done.html'),   
        name='password_change_done'),

    #forget password
    path('password_reset/', PasswordResetView.as_view(template_name ='blog/auth/password_reset.html'), 
        name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name ='blog/auth/password_reset_done.html'), 
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name ='blog/auth/password_reset_form.html', 
        ), 
        name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name ='blog/auth/password_reset_complete.html'),
        name='password_reset_complete'),
]