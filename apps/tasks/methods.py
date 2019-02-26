from django.shortcuts import redirect

from apps.tasks.models import Task


def execute(request, args: list):
    """
    Execute a tasks method with given arguments.
    """
    method = args[0]
    user = request.user
    if method == 'new':
        new_task(user, args[1:])
    elif method == 'rm':
        delete_task(user, args[1])

    return redirect('/tasks')


def new_task(user, data: []):
    """
    Create a new task and save it.
    """
    Task(user=user, description=data[0], due_time=data[1]).save()


def delete_task(user, task_id):
    """
    Delete a task by id, succeed only if user id matches.
    Other users should not be able to delete others records.
    """
    try:
        Task.objects.get(user=user, id=task_id).delete()
    except Exception as e:
        print(e)
