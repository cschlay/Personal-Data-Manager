from django.shortcuts import render, redirect

from lib.printer import format_currency


def index(request):
    user = request.user

    return render(request, 'budget.html')


"""
def submit(request):
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
"""
