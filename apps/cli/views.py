from django.shortcuts import redirect

from apps.library.functions import execute
from lib.parser import split_string_with_delimiter

from apps.tasks import methods as tasks
from apps.budget import methods as budget


def cli(request):
    if request.method == 'POST':
        command = split_string_with_delimiter(request.POST['command'], '\'')

        app = command[0]
        args = command[1:]
        if app == 'budget':
            return budget.execute(request, args)
        elif app == 'library':
            return execute(request, args)
        elif command[0] == 'tasks':
            return tasks.execute(request, args)

    return redirect('/')
