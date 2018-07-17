from django.http import QueryDict, HttpRequest
from django.shortcuts import redirect

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
        q.appendlist('category', args[2])
        q.appendlist('description', args[3])
        request.POST = q

        submit(request)

    return redirect('budget')
