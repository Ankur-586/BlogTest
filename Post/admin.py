from django.contrib import admin
from .models import Post

@admin.register(Post)
class postadmin(admin.ModelAdmin):
    list_display = ['id','title','author','content','created_on','status']

