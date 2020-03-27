from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import SignupForm

# Create your views here.

def Signup(request):

    if request.user.is_authenticated:
        return redirect('titles')
    else:

        form = SignupForm()

        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        return render(request, 'signup.html', {'form': form})
