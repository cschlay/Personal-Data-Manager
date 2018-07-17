from django.shortcuts import render, redirect

from apps.cli.functions import budget


def cli(request):
    command = request.POST['command'].split()

    if command[0] == "budget":
        return budget(request, command[1:])

    return redirect('library')
