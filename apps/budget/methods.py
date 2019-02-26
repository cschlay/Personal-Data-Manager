from datetime import datetime as time

from apps.budget.models import Spending, Income


def execute(request, args: list):
    method: str = args[0]


def get_income(request, year=time.now().year, month=time.now().month) -> int:
    """
    Return total income from a given time range.
    """
    total: int = 0
    for record in Income.objects.filter(user=request.user, date__year=year, date__month=month):
        total += record.amount
    return total


def get_spending(request, year=time.now().year, month=time.now().month) -> int:
    """
    Returns total spendings in a given time frame.
    """
    total: int = 0
    for record in Spending.objects.filter(user=request.user, date__year=year, date__month=month):
        total += record.amount
    return total
