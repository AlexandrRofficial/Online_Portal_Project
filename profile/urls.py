from django.urls import path
from .views import profill, pldesc

urlpatterns = [
    path('', profill, name='profile'),
    path('pldesc/', pldesc, name='pldesc'),
]
