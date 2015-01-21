from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blog.models import BlogPost

def index(request):
    return render(request, 'base.html', {
        'posts': BlogPost.objects.filter(display=True).order_by('created')[::-1],
        'heading': BlogPost.objects.filter(heading=True).order_by('created')[0]
        })

def entry(request, id):
    try:
        entry_ = BlogPost.objects.get(pk=id)
    except BlogPost.DoesNotExist:
        raise Http404
    return render(request, 'entry.html', {
        'entry': entry_,
    })
