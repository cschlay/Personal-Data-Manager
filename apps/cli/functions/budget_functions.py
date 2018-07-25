from django.http import QueryDict
from django.shortcuts import redirect

from apps.budget.models import Revenue, Spending, Category
from apps.budget.views import submit


def budget_functions(request, args):
    """

    :param argv: the arguments
    :return:
    """

    # Adding a earnings or a spending
    # budget add yyyy-mm-dd $amount $category $description
    if args[0] == 'push':
        q = QueryDict(mutable=True)
        q.appendlist('date', args[1])
        q.appendlist('amount', args[2])
        category = Category.objects.get(value=args[3])
        q.appendlist('category', category.id)
        q.appendlist('description', args[4])
        request.POST = q

        submit(request)

    if args[0] == 'pop':
        pop(args[1])

    return redirect('budget')


def pop(table: str):
    """
    Removes the latest input. To be used in case of a typo.

    :return: The removed record.
    """

    if table == 'spendings':
        return Spending.objects.last().delete()
    else:
        return Revenue.objects.last().delete()
