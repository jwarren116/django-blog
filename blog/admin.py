from django.contrib import admin
from blog.models import BlogPost


class UserAdmin(admin.ModelAdmin):
    fields = ['title', 'post', 'display', 'heading']
    list_display = ('id', 'title', 'post', 'created', 'display', 'heading')

admin.site.register(BlogPost, UserAdmin)
