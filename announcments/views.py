from .models import Announcement

from django.shortcuts import render

from .forms import AnnouncmentForm

def announcments(request):
    announcments = Announcement.objects.all()
    print(announcments)
    return render(request, 'announcments_main_page.html', context={"announcments": announcments})