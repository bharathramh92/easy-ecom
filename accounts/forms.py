from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from . import accounts_messages as ac_msg
from .models import Address

class LoginForm(forms.Form):

    username = forms.CharField(label='Username/Email',
                               max_length=100,
                               required= True)

    loginPassword = forms.CharField(widget= forms.PasswordInput,
                               label='Password',
                               max_length=20,
                               required= True)

    def clean_username(self):
        username = self.cleaned_data['username']
        if '@' in username:
            try:
                username = User.objects.get(email=username).username
            except Exception:
                raise forms.ValidationError((ac_msg.login_wrong_username_password), code='invalid')
        return username

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


class EmailForm(forms.Form):

    email = forms.EmailField(label='Email',
                               max_length=100,
                               required= True)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email = email)
        except Exception:
            self.add_error('email', ac_msg.email_not_found)
        return email

class ForgotPasswordForm(forms.Form):

    password = forms.CharField(widget= forms.PasswordInput,
                               label='Password',
                               max_length=20,
                               required= True)

    confirmPassword = forms.CharField(widget= forms.PasswordInput,
                               label='Confirm Password',
                               max_length=20,
                               required= True)

    def clean(self):
        cleaned_data = super(ForgotPasswordForm, self).clean()

        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')

        if password != confirmPassword:
            self.add_error('password', ac_msg.registration_passwords_not_matching)

        return cleaned_data

class ChangePasswordForm(forms.Form):

    currentPassword = forms.CharField(widget= forms.PasswordInput,
                               label='Current Password',
                               max_length=20,
                               required= True)

    newPassword = forms.CharField(widget= forms.PasswordInput,
                               label='New Password',
                               max_length=20,
                               required= True)

    confirmNewPassword = forms.CharField(widget= forms.PasswordInput,
                               label='Confirm New Password',
                               max_length=20,
                               required= True)

    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user')
        super(ChangePasswordForm,self).__init__(*args,**kwargs)

    def clean(self):
        print("user in form ", self.user)
        cleaned_data = super(ChangePasswordForm, self).clean()
        currentPassword = cleaned_data.get('currentPassword')
        newPassword = cleaned_data.get('newPassword')
        confirmNewPassword = cleaned_data.get('confirmNewPassword')

        if not self.user.check_password(currentPassword):
            self.add_error('currentPassword', ac_msg.wrong_current_password)

        if newPassword != confirmNewPassword:
            self.add_error('newPassword', ac_msg.registration_passwords_not_matching)

        return cleaned_data


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user', 'last_updated_datetime', 'added_datetime']