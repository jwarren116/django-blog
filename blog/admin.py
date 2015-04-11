from django.contrib import admin
from blog.models import BlogPost, Project


class UserAdmin(admin.ModelAdmin):
    fields = ['title', 'post', 'display']
    list_display = ('id', 'title', 'post', 'created', 'display')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'display')

admin.site.register(BlogPost, UserAdmin)
admin.site.register(Project, ProjectAdmin)
