from datetime import datetime

from django.shortcuts import render, redirect


# Create your views here.
from apps.budget.functions import to_printable_currency, get_monthly_earnings, get_monthly_spending
from apps.dashboard.models import TimeAllocation


def index(request):
    if request.user.is_authenticated:
        try:
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
            time_as_percentage = ((total_hours - hours_consumed) / total_hours) * 100

            # Calculate money spent this month.

            context = {
                'user': user,
                'hours_left': hours_left,
                'time_as_percentage': time_as_percentage,
                'spending': to_printable_currency(str(get_monthly_spending())),
                'earnings': to_printable_currency(str(get_monthly_earnings()))
            }

            return render(request, 'dashboard.html', context)
        except Exception as e:
            return redirect('settings')
    else:
        return redirect('login')


def settings(request):
    context = {}

    if request.method == 'POST':
        print(request.POST['start-date'])

        t = TimeAllocation(user=request.user, start_date=request.POST['start-date'], retire_date=request.POST['end-date'])
        t.save()
        context['message'] = 'saved'
    else:
        context['message'] = None

    return render(request, 'settings.html', context)
