from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserExtended
from constants import accounts_messages as ac_msg
from ecom_functions import random_alphanumeric as ran
# Create your views here.
def loginView(request):
    # if this is a POST request we need to process the form data
    login_error_messages, register_error_messages = [], []
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if 'login' in request.POST:
            loginForm = LoginForm(request.POST)
            if loginForm.is_valid():
                username = loginForm.cleaned_data['username']
                loginPassword = loginForm.cleaned_data['loginPassword']
                user = authenticate(username= username, password=loginPassword)
                if user is not None:
                    # the password verified for the user
                    if user.is_active:
                        login(request, user)
                        # print("User is valid, active and authenticated")
                        return HttpResponseRedirect(reverse('accounts:dashboard'))
                    else:
                        login_error_messages.append(ac_msg.account_disabled)
                        # print("The password is valid, but the account has been disabled!")
                else:
                    # the authentication system was unable to verify the username and password
                    login_error_messages.append(ac_msg.wrong_username_password)
                    # print("username/password combination was incorrect")

            registerForm = RegisterForm()
        elif 'register' in request.POST:
            registerForm = RegisterForm(request.POST)
            if registerForm.is_valid():
                password = registerForm.cleaned_data['password']
                email = registerForm.cleaned_data['email']
                firstName = registerForm.cleaned_data['firstName']
                lastName = registerForm.cleaned_data['lastName']
                while(True):
                    try:
                        username = ran.rand_from_name(firstName, lastName)
                        user = User.objects.create_user(username, email=email, password=password)
                        user.first_name = firstName
                        user.last_name = lastName
                        user.save()
                        break
                    except Exception as e:
                        print(e)
                return HttpResponseRedirect(reverse('accounts:dashboard'))

            loginForm = LoginForm()
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
    # if a GET (or any other method) we'll create a blank form
    else:
        loginForm = LoginForm()
        registerForm = RegisterForm()

    # template = Template('Hello {{ name }}!')
    # template.render({'knights': 'that say nih'})
    return render(request, "accounts/login.html",{'loginForm' : loginForm, 'registerForm' : registerForm, 'login_error_messages' : login_error_messages, 'register_error_messages': register_error_messages})

@login_required()
def dashboardView(request):
    return render(request, "accounts/dashboard.html",{})

@login_required()
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:logout'))