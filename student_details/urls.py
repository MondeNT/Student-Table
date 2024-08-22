from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/add/', views.student_create, name='student_create'),
    
]