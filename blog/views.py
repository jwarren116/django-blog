from django.shortcuts import render
from django.http import Http404
from blog.models import BlogPost, Project


def index(request):
    return render(request, 'index.html', {
        'projects': Project.objects.filter(display=True).order_by('-id'),
        'posts': BlogPost.objects.filter(display=True).order_by('-created')[:8],
    })


def entry(request, id):
    try:
        entry = BlogPost.objects.get(pk=id)
    except BlogPost.DoesNotExist:
        raise Http404
    return render(request, 'entry.html', {
        'entry': entry,
    })


def posts(request):
    return render(request, 'posts.html', {
        'posts': BlogPost.objects.order_by('-created')
    })
