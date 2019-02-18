from django.shortcuts import render

from apps.tasks.models import Task


def index(request):
    """
    This is the main view of tasks app.
    Everything should be visible on modifiable in this one page.
    """
    tasks = Task.objects.get(user=request.user.id)

    context = {
        'tasks': tasks
    }

    return render(request, 'recipes.html', context)
