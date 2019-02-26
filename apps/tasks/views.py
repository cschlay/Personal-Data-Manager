from django.shortcuts import render

from apps.tasks.models import Task


def index(request):
    context = {
        'tasks': Task.objects.filter(user=request.user)
    }
    return render(request, 'tasks.html', context)
