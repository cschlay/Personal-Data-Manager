from django.shortcuts import redirect, render_to_response

# The actual index.html is never shown in personal use.

def index(request):
    if request.user.is_authenticated:
        user = request.user

        context = {'user': user}
        return render_to_response('dashboard.html', context)
    else:
        return redirect('login')
