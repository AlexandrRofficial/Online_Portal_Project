from django.urls import path
from .views import profill

urlpatterns = [
    path('', profill, name='profile'),
]
