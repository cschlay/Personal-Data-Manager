from django.shortcuts import render, redirect

from apps.budget.functions import to_printable_currency
from apps.budget.models import Revenue, Spending, Category


def budget(request):
    user = request.user

    revenues = Revenue.objects.filter(user=user).order_by('date')
    spending = Spending.objects.filter(user=user).order_by('date')

    context = {
        'user': user,
        'revenues': reversed(revenues),
        'spending': reversed(spending)
    }

    # Add the comma to currency.
    for record in revenues:
        record.amount = to_printable_currency(str(record.amount))

    for record in spending:
        record.amount = to_printable_currency(str(record.amount))

    return render(request, 'budget.html', context)


def submit(request):
    """
    Add new revenue record to database.

    :param request:
    """
    a = request.POST['amount']
    a = a[:len(a)-3] + a[len(a)-2:]

    print(request.POST['date'])

    if a[0] == '-':
        record = Spending()
    else:
        record = Revenue()

    record.user = request.user
    record.date=request.POST['date']
    record.amount=int(a)
    record.description = request.POST['description']

    if request.POST['category'] == '':
        record.category = Category()
    else:
        record.category = Category.objects.get(id=request.POST['category'])

    record.save()

    return redirect('budget')
