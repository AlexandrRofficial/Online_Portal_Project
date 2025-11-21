from django.urls import path
from .views import announcments

urlpatterns = [
    path('', announcments, name='announcments_main_page'),
]