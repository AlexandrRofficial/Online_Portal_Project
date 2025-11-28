from django.shortcuts import render
from .models import profile


def profill(request):
    profil = profile.objects.all()
   
    return render(request, 'profile.html', context={'profil': profil})
# Create your views here.


# Create your views here.
