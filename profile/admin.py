from django.contrib import admin
from .models import profile, post
from .forms import PostForm

class ProductAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ("post",)

admin.site.register(profile)
admin.site.register(post, ProductAdmin)

# Register your models here.
