from django.shortcuts import render, redirect

from apps.budget.models import Account


def budget(request):
    return render(request, 'budget.html')


def new_account(request):
    query = request.GET
    name = query.__getitem__('name')

    account = Account(user=request.user, account_name=name)
    account.save()

    return redirect('index')
