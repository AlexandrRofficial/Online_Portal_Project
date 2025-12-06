from django.shortcuts import render, redirect
from .models import profile, post
from .forms import PostForm


def profill(request):
    profil = profile.objects.all()
    postr = post.objects.all()
   
    return render(request, 'profile.html', context={'profil': profil, 'postr': postr})



def pldesc(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = PostForm()

    return render(request, 'pldesc.html', {"form": form})

def postt(request):
    postr = post.objects.all()
    return render(request, 'profile.html', context={'postr': postr})

def post_list(request):
    postr = post.objects.all()
    return render(request, 'profile.html', context={'postr': postr})

def cr_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = PostForm()

    return render(request, "pldesc.html", {"form": form})
 

# Create your views here.
