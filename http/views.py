from django.shortcuts import render


def http(request):
    return render(request, 'http.html', {
        'http_headers': request.META,
        'cookies': request.COOKIES,
        })
