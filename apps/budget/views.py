from django.shortcuts import render, redirect

from apps.budget.models import Revenue, Spending


def budget(request):
    user = request.user

    revenues = Revenue.objects.filter(user=user).order_by('date')
    spendings = Spending.objects.filter(user=user).order_by('date')

    context = {
        'user': user,
        'revenues': reversed(revenues),
        'spendings': reversed(spendings)
    }

    # Add the comma to currency.
    for record in revenues:
        a = str(record.amount)
        record.amount = a[:len(a)-2] + ',' + a[len(a)-2:]

    for record in spendings:
        a = str(record.amount)
        record.amount = a[:len(a)-2] + ',' + a[len(a)-2:]

    return render(request, 'budget.html', context)


def submit(request):
    """
    Add new revenue record to database.

    :param request:
    """
    a = request.POST['amount']
    a = a[:len(a)-3] + a[len(a)-2:]

    if a[0] == '-':
        record = Spending(
            user=request.user,
            date=request.POST['date'],
            amount=int(a),
            comment=request.POST['comment']
        )
    else:
        record = Revenue(
            user=request.user,
            date=request.POST['date'],
            amount=int(a),
            comment=request.POST['comment']
        )
    record.save()

    return redirect('budget')
