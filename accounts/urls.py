from django.contrib import admin
from django.urls import path,include
from . import views
app_name  = 'accounts_app'
urlpatterns = [
    path('logout/',views.user_logout,name='user_logout'),
    path('login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
   
]
