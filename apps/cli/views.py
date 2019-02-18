# Copyright (c) 2018 C. H. Lay
# MIT License


from django.shortcuts import redirect

from apps.cli.functions.budget_functions import budget_functions
from apps.library.functions import execute
from lib.parser import split_string_with_delimiter


def cli(request):
    command = split_string_with_delimiter(request.POST['command'], '\'')

    if command[0] == 'budget':
        return budget_functions(request, command[1:])
    elif command[0] == 'library':
        return execute(request, command[1:])

    return redirect(request, 'library')
