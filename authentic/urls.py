from django.urls import path
from .import views

urlpatterns =[
    path('',views.Register_user, name='register'),
    path('login',views.loginUser,name='login'),
]