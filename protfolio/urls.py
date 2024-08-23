from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('projectadd/', views.add_project, name='add_project'),
    path('project/edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('project/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('list_project/', views.list_projects, name='list_projects'),
    path('work_experience/', views.list_work_experience, name='list_work_experience'),
    path('education/', views.list_education, name='list_education'),
    path('certifications/', views.list_certifications, name='list_certifications'),
    path('',views.project,name='index'),
    path('profile_create/',views.profile_create,name='profilecreate'),
]

