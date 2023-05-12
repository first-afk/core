from django.urls import path
from core import views

urlpatterns = [
    path('', views.index),
    path('new/', views.welcome),
    path('settings/', views.settings),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('logout/', views.logout),
]