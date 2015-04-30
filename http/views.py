from django.shortcuts import render


def http(request):
    return render(request, 'http.html', {
        'request': request,
        })
