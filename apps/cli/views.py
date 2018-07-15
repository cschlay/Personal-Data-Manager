from django.shortcuts import render, redirect


def cli(request):
    print(request.POST['command'])

    return redirect('library')
