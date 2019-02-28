from django.shortcuts import render, redirect

from apps.budget.models import Income, Spending
from lib.printer import format_currency


def index(request):
    user = request.user
    context = {
        'income': Income.objects.filter(user=user),
        'spending': Spending.objects.filter(user=user)
    }
    for x in context['income']:
        x.amount = format_currency(x.amount)

    for x in context['spending']:
        x.amount = format_currency(x.amount)

    return render(request, 'budget.html', context)

