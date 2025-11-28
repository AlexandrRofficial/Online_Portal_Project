from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students'),
    path('add_logics/', views.add_logics, name='add_logics'),
]