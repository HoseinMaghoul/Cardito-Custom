from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('category/<int:c_id>/', views.category, name='category'),
    path('projects', views.projects, name='projects'),
    path('project/<int:p_id>', views.project, name='project'),
    
]