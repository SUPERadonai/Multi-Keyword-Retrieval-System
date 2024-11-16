from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard_hou', views.dashboard_house, name='dashboard_house'),
    path('dashboard_fav', views.dashboard_fav, name='dashboard_fav'),
]
