from django.shortcuts import render


def start(request):
    context = {}
    return render(request, 'core/start.html', context)
