from django.shortcuts import redirect, render

# The actual index.html is never shown in personal use.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')
