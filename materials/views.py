from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item
import os
def materials_list(request):
    items = Item.objects.all().order_by("-id")
    return render(request, 'materials/materials_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('materials_list')
    else:
        form = ItemForm()
    return render(request, 'materials/add_item.html', {'form': form})
