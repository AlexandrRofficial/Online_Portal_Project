from django.shortcuts import render
from .models import profile


def profill(request):
    profil = profile.objects.all()
   
    return render(request, 'profile.html', context={'profil': profil})


def pldesc(request):
    return render(request, 'pldesc.html')


# Create your views here.
