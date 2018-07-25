from django.shortcuts import  redirect
from apps.cli.functions.budget_functions import budget_functions
from apps.cli.functions.library_functions import library_functions


def cli(request):
    command = request.POST['command'].split()

    if command[0] == 'budget':
        return budget_functions(request, command[1:])
    elif command[0] == 'library':
        return library_functions(request, command[1:])

    return redirect('library')
