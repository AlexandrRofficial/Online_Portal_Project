from django.contrib import admin

from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'logics')

admin.site.register(Student, StudentAdmin)