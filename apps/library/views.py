from django.shortcuts import render, redirect

from apps.library.models import Book


def index(request):
    context = {'books':  Book.objects.filter(user=request.user)}

    return render(request, 'library.html', context)


def book(request, book_id):
    """
    Individual book page displaying the progress of its exercises if they exists.

    :param book_id:
    :param request:
    :return:
    """
    context = {
        'book': Book.objects.get(user=request.user, id=book_id)
    }

    return render(request, 'book.html', context)


def submit(request):
    record = Book(
        user=request.user,
        title=request.POST['title'],
        subtitle=request.POST['subtitle'],
        author=request.POST['author'],
        edition=request.POST['edition'],
        read=True if request.POST['read'] == 'on' else False
    )
    record.save()

    return redirect('library')