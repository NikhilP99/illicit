from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<p>testing 1 2 3</p>")
