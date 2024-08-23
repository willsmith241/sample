from django.urls import path
from .import views

urlpatterns = [
    path('profiles/', views.profile_view, name='profile_view'),
    path('about/',views.about_view,name='about'),
    path('hom',views.hom,name='hom'),
    path('project/',views.project,name='project')

]