from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students'),
    path('add_logic/<int:student_id>/', views.add_logic, name='add_logic'),
]