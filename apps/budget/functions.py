# MIT License
# Copyright (c) 2018 C. H. Lay
from datetime import datetime

from apps.budget.models import Spending, Revenue


def get_monthly_spending():
    t = datetime.now()

    total: int = 0
    for r in Spending.objects.filter(date__year=t.year, date__month=t.month):
        total += r.amount

    return total


def get_monthly_earnings():
    t = datetime.now()

    total: int = 0
    for r in Revenue.objects.filter(date__year=t.year, date__month=t.month):
        total += r.amount

    return total


def to_printable_currency(value: str):
    if value == '0':
        return '0'
    else:
        return value[:len(value) - 2] + ',' + value[len(value) - 2:]