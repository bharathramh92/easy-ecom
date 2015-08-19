from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from ecom_functions import random_alphanumeric as ran
from django.core.mail import send_mail, EmailMessage
from easy_ecom import settings_sensitive
from django.contrib.auth.decorators import login_required
from .forms import StoreSelectForm, NewBookForm, ISBNCheckForm, ItemForm
from store.models import BookStore

# Create your views here.
@login_required()
def dashboardView(request):
    return render(request, 'sell/dashboard.html', {})

@login_required()
def newView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StoreSelectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(request.POST.get('store_names'))
            if request.POST.get('store_names') == 'Books':
                return HttpResponseRedirect(reverse('sell:newBookCheck'))

            return HttpResponseRedirect(reverse('sell:new'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StoreSelectForm()

    return render(request, "sell/new.html", {'storeForm': form})

@login_required()
def editView(request):
    return HttpResponse("seller editView")

@login_required()
def addNewBook(request, isbn):

    try:
        BookStore.objects.get(pk=isbn)
        raise PermissionDenied
    except Exception:
        pass

    # if this is a POST request we need to process the form data
    print("ISBN is " + isbn)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        bookForm = NewBookForm(request.POST)
        itemForm = ItemForm(request.POST)
        # check whether it's valid:
        if bookForm.is_valid() and itemForm.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            return HttpResponseRedirect('done')

    # if a GET (or any other method) we'll create a blank form
    else:
        bookForm = NewBookForm()
        itemForm = ItemForm()
    return render(request, "sell/new_book.html", {'bookForm' : bookForm, 'itemForm': itemForm})

@login_required()
def addNewBookPKCheck(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ISBNCheckForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            isbn = form.cleaned_data['isbn']
            try:
                BookStore.objects.get(pk=isbn)
                #if found, redirect him to add as a seller in the listing
                print("add him to the inventory")
            except Exception:
                #if not found, create a new book
                return HttpResponseRedirect(reverse('sell:newBook', kwargs= {'isbn' : isbn}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ISBNCheckForm()

    return render(request, "sell/new_book.html", {'bookForm': form})