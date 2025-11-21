from django.shortcuts import render

def announcments(request):
    return render(request, 'announcments_main_page.html')