from django.shortcuts import redirect, render_to_response

# The actual index.html is never shown in personal use.
from apps.budget.models import Account


def index(request):
    if request.user.is_authenticated:
        user = request.user

        return render_to_response('dashboard.html', {'user' : user,
                                                     'accounts' : Account(user.id)})
    else:
        return redirect('login')
