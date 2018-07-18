from django.http import QueryDict
from django.shortcuts import redirect

from apps.budget.models import Category
from apps.budget.views import submit


def budget(request, args: []):
    """

    :param argv: the arguments
    :return:
    """

    # Adding a earnings or a spending
    # budget add yyyy-mm-dd $amount $category $description
    if len(args) == 4:
        q = QueryDict(mutable=True)
        q.appendlist('date', args[0])
        q.appendlist('amount', args[1])
        category = Category.objects.get(value=args[2])
        q.appendlist('category', category.id)
        q.appendlist('description', args[3])
        request.POST = q

        submit(request)

    return redirect('budget')
