# MIT License
# Copyright (c) 2018 C. H. Lay
from django.shortcuts import redirect

from apps.library.models import Book


def execute(request, command: [str]):
    """
    Selects and executes a proper function call.

    :param request:
    :param command:
    :return:
    """
    if command[0] == 'add':
        add_book(request, command[1:])
    elif command[0] == 'pop':
        delete_latest()

    return redirect('library')


def add_book(request, details: [str]):
    """
    Add a new book to database with basic info.

    :param details:
    :param request:
    :return:
    """
    record = Book(
        user=request.user,
        title=details[0],
        read=details[1] == 'True',
        hasExercises=details[2] == 'True'
    )

    record.save()


def delete_latest():
    """
    Delete the latest record.
    """
    Book.objects.last().delete()
