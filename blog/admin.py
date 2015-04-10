from django.contrib import admin
from blog.models import BlogPost, Project


class UserAdmin(admin.ModelAdmin):
    fields = ['title', 'post', 'display']
    list_display = ('id', 'title', 'post', 'created', 'display')

admin.site.register(BlogPost, UserAdmin)
admin.site.register(Project)
