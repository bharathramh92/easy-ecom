from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from .forms import LoginForm, RegisterForm, EmailForm, ForgotPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from constants import accounts_messages as ac_msg
from ecom_functions import random_alphanumeric as ran
from django.core.mail import send_mail, EmailMessage
from easy_ecom import settings_sensitive
from .models import EmailVerification, ForgotPasswordVerification, UserExtended

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
                        if not user.userextended.is_email_verified:
                            return render(request, "accounts/email_not_verified.html",{})
                        login(request, user)
                        # print("User is valid, active and authenticated")
                        return HttpResponseRedirect(reverse('accounts:dashboard'))
                    else:
                        login_error_messages.append(ac_msg.login_account_disabled)
                        # print("The password is valid, but the account has been disabled!")
                else:
                    # the accounts system was unable to verify the username and password
                    login_error_messages.append(ac_msg.login_wrong_username_password)
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
                        username = ran.rand_from_name(firstName.lower(), lastName.lower())          #generating username
                        user = User.objects.create_user(username, email=email, password=password)
                        break
                    except Exception:
                        pass
                user.first_name = firstName
                user.last_name = lastName
                user.save()
                UserExtended(user = user).save()
                send_verification_email(user)
                return render(request, "accounts/new_user_registered.html",{})

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

def send_verification_email(user):
    try:
        result = EmailVerification.objects.get(user = user)
        if result.is_not_expired_email_verification:            #if verification code is not expired, send the same code, and set the email send time to now
            result.sent_datetime = timezone.now()
            result.save()
            verification_code = result.verification_code
        else:                                                   #if expired, delete the previous code
            result.delete()
            raise Exception
    except Exception:
        verification_code = ran.rand_alphanumeric()
        email_ver_storage = EmailVerification.objects.create(user=user, verification_code = verification_code)

    email_msg = ac_msg.registration_email_verfication
    email_msg += "http://127.0.0.1:8000" + reverse('accounts:verify', kwargs= {'verification_code' : verification_code, 'username' : user.username})
    send_mail('Verify your email', email_msg, settings_sensitive.EMAIL_HOST_USER, [user.email], fail_silently=True)


def send_forgot_password_verification_email(user):
    try:
        result = ForgotPasswordVerification.objects.get(user = user)
        if result.is_not_expired_email_verification:            #if verification code is not expired, send the same code, and set the email send time to now
            result.sent_datetime = timezone.now()
            result.save()
            verification_code = result.verification_code
        else:                                                   #if expired, delete the previous code
            result.delete()
            raise Exception
    except Exception:
        verification_code = ran.rand_alphanumeric()
        forgot_password_ver_storage = ForgotPasswordVerification.objects.create(user=user, verification_code = verification_code)

    email_msg = ac_msg.forgot_password_message
    email_msg += "http://127.0.0.1:8000" + reverse('accounts:forget_password_check')+ "?verification_code=" +  verification_code + '&username=' +  user.username
    send_mail('Reset Password', email_msg, settings_sensitive.EMAIL_HOST_USER, [user.email], fail_silently=True)


@login_required()
def dashboardView(request):
    return render(request, "accounts/dashboard.html",{})

@login_required()
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:logout'))

def emailVerificationCheckView(request, verification_code, username):
    if request.user.is_authenticated() and request.user.userextended.is_email_verified:   #in case user clicks more than one email verification link
         return HttpResponseRedirect(reverse('accounts:dashboard'))
    try:
        result = EmailVerification.objects.get(user__username = username, verification_code = verification_code)
        if not result.is_not_expired_email_verification:
                raise Exception
    except Exception:
        return render(request, "accounts/invalid_verification_email.html",{})

    user = User.objects.get(username = username)
    user.userextended.is_email_verified = True
    user.userextended.save()
    result.delete()
    return render(request, "accounts/email_verified.html",{})

# (?P<username>[\w]*)/(?P<verification_code>[a-z0-9]*)
def forgotPasswordCheckView(request):
    if request.user.is_authenticated():   #only if the user didn't login
         return HttpResponseRedirect(reverse('accounts:dashboard'))

    verification_code, username = request.GET.get('verification_code'), request.GET.get('username')
    if verification_code == None or username == None:
        return render(request, "accounts/invalid_forgot_password_reset.html",{})
    else:
        try:
            result = ForgotPasswordVerification.objects.get(user__username = username, verification_code = verification_code)
            if not result.is_not_expired_forgot_password:
                raise Exception
        except Exception:
            return render(request, "accounts/invalid_forgot_password_reset.html",{})

    user = User.objects.get(username = username)


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ForgotPasswordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            result.delete()
            return render(request, "accounts/forgot_password_reset_done.html",{})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ForgotPasswordForm()

    return render(request, 'accounts/forgot_password_reset.html',
                  {'form': form, 'verification_code' : verification_code, 'username' : username})

def troubleLoginView(request):
    if request.user.is_authenticated():   #trouble login is for forgot password and resend verification alone
         return HttpResponseRedirect(reverse('accounts:dashboard'))
    return render(request, "accounts/trouble_login.html",{})

def forgetPasswordView(request):
    if request.user.is_authenticated():   #forgot password is only if user couldn't login
         return HttpResponseRedirect(reverse('accounts:dashboard'))
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            if not user.userextended.is_email_verified:
                return render(request, "accounts/resend_verification_email.html", {'already_verified': False})
            send_forgot_password_verification_email(user)
            return render(request, "accounts/forgot_password.html", {'success': True})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, "accounts/forgot_password.html", {'form': form, 'already_verified': True})

def resendVerificationEmailView(request):
    # if this is a POST request we need to process the form data
    if request.user.is_authenticated():       #only if the no user logged
         return HttpResponseRedirect(reverse('accounts:dashboard'))

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            if user.userextended.is_email_verified:
                return render(request, "accounts/resend_verification_email.html", {'already_verified': True})
            send_verification_email(user)
            return render(request, "accounts/resend_verification_email.html", {'success': True})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, "accounts/resend_verification_email.html", {'form': form})