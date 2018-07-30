from datetime import datetime, date

from django.shortcuts import redirect, render_to_response

# The actual index.html is never shown in personal use.
from apps.budget.api import get_monthly_spending, get_monthly_earnings, to_printable_currency
from apps.lobby.models import TimeAllocation


def index(request):
    if request.user.is_authenticated:
        user = request.user
        time_allocation = TimeAllocation.objects.get(user=user.id)

        start_date = time_allocation.start_date
        retire_date = time_allocation.retire_date

        # Calculate Total Hours retire - start
        total_hours = (retire_date - start_date).days * 24

        # Calculate Hours Consumed.
        hours_consumed = (datetime.now().date() - start_date).days * 24
        hours_left = total_hours - hours_consumed

        # Transform to percentage.
        time_as_percentage = (total_hours - hours_consumed) / total_hours * 100

        # Calculate money spent this month.


        context = {
            'user': user,
            'hours_left': hours_left,
            'time_as_percentage': time_as_percentage,
            'spending': to_printable_currency(str(get_monthly_spending())),
            'earnings': to_printable_currency(str(get_monthly_earnings()))
        }

        return render_to_response('dashboard.html', context)
    else:
        return redirect('login')
