from django.shortcuts import render

from .models import Announcement

def announcments(request):
    announcments = Announcement.objects.all()

    important = request.GET.get("important")
    if important == "true":
        announcments = announcments.filter(important=True)
    elif important == "false":
        announcments = announcments.filter(important=False)

    sort = request.GET.get("sort")
    if sort == "created_at_asc":
        announcments = announcments.order_by("created_at")
    elif sort == "created_at_desc":
        announcments = announcments.order_by("-created_at")
    elif sort == "important_first":
        announcments = announcments.order_by("-important", "-created_at")

    return render(request, "announcments_main_page.html", {
        "announcments": announcments
    })