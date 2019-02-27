from datetime import datetime

from django.shortcuts import render, redirect


from apps.budget.methods import get_spending, get_income
from apps.dashboard.models import TimeAllocation
from apps.tasks.models import Task
from lib.printer import format_currency


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
                'spending': format_currency(get_spending(request)),
                'income': format_currency(get_income(request)),
                'tasks': Task.objects.filter(user=user).order_by('due_time')
            }
            return render(request, 'dashboard.html', context)
        except Exception as e:
            print(e)
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
