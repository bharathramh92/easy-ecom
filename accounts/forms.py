from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from constants import accounts_messages as ac_msg

class LoginForm(forms.Form):

    username = forms.CharField(label='Username/Email',
                               max_length=100,
                               required= True)

    loginPassword = forms.CharField(widget= forms.PasswordInput,
                               label='Password',
                               max_length=20,
                               required= True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        print("login form test")

def doesEmailExists(email):
    try:
        if len(User.objects.filter(email = email)) == 0:        #incase more than one user got created accidentaly with same email earlier
            return False
        raise Exception
    except Exception as e:
        return True

class RegisterForm(forms.Form):

    email = forms.EmailField(label='Email',
                               max_length=100,
                               required= True)

    firstName = forms.CharField(label='First Name',
                               max_length=30,
                               required= True,
                               min_length= 2)

    lastName = forms.CharField(label='Last Name',
                               max_length=30,
                               required= True,
                               min_length= 2)

    password = forms.CharField(widget= forms.PasswordInput,
                               label='Password',
                               max_length=20,
                               required= True)

    confirmPassword = forms.CharField(widget= forms.PasswordInput,
                               label='Confirm Password',
                               max_length=20,
                               required= True)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')


        if doesEmailExists(email):
            self.add_error('email', ac_msg.registration_same_email_address)

        if password != confirmPassword:
            self.add_error('password', ac_msg.registration_passwords_not_matching)

        return cleaned_data