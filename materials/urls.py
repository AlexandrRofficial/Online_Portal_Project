from django.urls import path
from .views import materials_list, add_item

urlpatterns = [
    path('', materials_list, name='materials_list'),
    path('add/', add_item, name='add_item'),
]