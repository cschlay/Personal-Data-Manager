from django.shortcuts import redirect

from apps.library.models import Book


def library_functions(request, args: []):
    if args[0] == 'push':
        push(request.user, args[1:])

    return redirect('library')


def push(user, args: []):
    record = Book(
        user=user,
        title=args[0], # How to parse title and author?
        author=args[1],
        edition=args[2],
        read=True if args[3] == 'true' else False)

    record.save()