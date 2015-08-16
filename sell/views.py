from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from ecom_functions import random_alphanumeric as ran
from django.core.mail import send_mail, EmailMessage
from easy_ecom import settings_sensitive
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def dashboardView(request):
    return HttpResponse("seller dashboard")

@login_required()
def newView(request):
    return HttpResponse("seller newView")

@login_required()
def editView(request):
    return HttpResponse("seller editView")