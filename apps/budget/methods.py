from datetime import datetime as time
from typing import Union

from django.shortcuts import redirect

from apps.budget.models import Spending, Income, ItemType, Item, IncomeType
from lib.parser import currency_to_int


def execute(request, args: list):
    method: str = args[0]
    {
        'new-item': new_item,
        'new-item-type': new_item_type,
        'new-source': new_income_type,
        'income': log_income,
    }[method](request, args[1:])

    return redirect('/budget')


def log_income(request, args: list):
    """
    Log a new income record.
    """
    amount: int = currency_to_int(args[1])
    type_name: str = args[2]

    if not IncomeType.objects.filter(name=type_name).exists():
        new_income_type(request, [type_name])
    income_type: IncomeType = IncomeType.objects.get(name=type_name)

    Income(user=request.user, date=args[0], amount=amount, type=income_type).save()


def new_item_type(request, name: Union[list, str]):
    """
    Add new item type to database.
    """
    if name is list:
        return ItemType(name=name[0]).save()
    elif name is str:
        return ItemType(name=name).save()


def new_item(request, args: list):
    Item(name=args[1], type=ItemType.objects.get(name=args[0])).save()


def new_income_type(request, args: list) -> IncomeType:
    name: str = args[0]
    try:
        IncomeType.objects.get(name=name)
    except IncomeType.DoesNotExist:
        IncomeType(name=name).save()


def get_income(request, year: int = time.now().year, month: int = time.now().month) -> int:
    """
    Return total income from a given time range.
    """
    total: int = 0
    print(year)
    print(month)
    for record in Income.objects.filter(user=request.user, date__year=year, date__month=month):
        print(record.amount)
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
