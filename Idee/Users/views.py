from django.shortcuts import redirect
from users.forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# views

def signup(request):
    signup_form = SignupForm(data=request.POST)
    if request.method == 'POST':
        if signup_form.is_valid():
            username = signup_form.clean_username()
            password = signup_form.clean_passwordconfirm()
            signup_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return signup(request, signup_form=signup_form)
    return redirect('/')