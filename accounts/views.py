from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import UserForm

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user)

            return redirect('accounts:dashboard')

    else:
        form = UserForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)



@login_required
def dashboard(request):
    user = request.user

    return render(request, 'accounts/dashboard.html', context={
        'user': user,
    })
