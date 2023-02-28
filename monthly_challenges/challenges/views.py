from django.http import HttpResponse


def january(request):
    return HttpResponse("Eat no meat for the entire month!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")
