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
from .forms import StoreSelectForm, NewBookForm, NewBookISBNCheckForm, ItemForm, NewBookAuthorForm, NewBookPublisherForm
from store.models import BookStore, Item, Author, Publisher
from django.core.exceptions import ObjectDoesNotExist

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
        if len(str(int(isbn))) == 13:       #double checking isbn format, since a direct request to this url could break our desired outcome.
            BookStore.objects.get(pk=isbn)
        else:
            raise PermissionDenied
    except ObjectDoesNotExist:
        pass
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        bookForm = NewBookForm(request.POST)
        itemForm = ItemForm(request.POST, store="Books")
        authorForm = NewBookAuthorForm(request.POST)
        publisherForm = NewBookPublisherForm(request.POST)
        # check whether it's valid:
        if bookForm.is_valid() and itemForm.is_valid() and authorForm.is_valid() and publisherForm.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            title = itemForm.cleaned_data['title']
            description = itemForm.cleaned_data['description']
            brand = itemForm.cleaned_data['brand']
            shipping_product_dimension_height = itemForm.cleaned_data['shipping_product_dimension_height']
            shipping_product_dimension_width = itemForm.cleaned_data['shipping_product_dimension_width']
            shipping_product_dimension_length = itemForm.cleaned_data['shipping_product_dimension_length']
            shipping_product_dimension_units = itemForm.cleaned_data['shipping_product_dimension_units']
            shipping_product_weight = itemForm.cleaned_data['shipping_product_weight']
            shipping_product_weight_units = itemForm.cleaned_data['shipping_product_weight_units']
            category = itemForm.cleaned_data['category']
            item = Item.objects.create(title= title, description= description, brand= brand, shipping_product_dimension_height= shipping_product_dimension_height,
                               shipping_product_dimension_width= shipping_product_dimension_width, shipping_product_dimension_length= shipping_product_dimension_length,
                               shipping_product_dimension_units= shipping_product_dimension_units, shipping_product_weight= shipping_product_weight,
                               shipping_product_weight_units= shipping_product_weight_units)
            item.category.add(*category)

            isbn_10 = bookForm.cleaned_data['isbn_10']
            isbn_13 = bookForm.cleaned_data['isbn_13']
            language = bookForm.cleaned_data['language']
            book_type = bookForm.cleaned_data['book_type']
            book_condition = bookForm.cleaned_data['book_condition']
            publisher = publisherForm.cleaned_data['name']

            book = BookStore.objects.create(isbn_10=isbn_10, isbn_13=isbn_13, language=language, book_type=book_type,
                                           book_condition= book_condition, item=item, publisher= publisher)
            authors = authorForm.cleaned_data['name']
            book.authors.add(*authors)

            return HttpResponseRedirect(reverse('sell:newInventory'))
    # if a GET (or any other method) we'll create a blank form
    else:
        bookForm = NewBookForm()
        itemForm = ItemForm(store="Books")
        authorForm = NewBookAuthorForm()
        publisherForm = NewBookPublisherForm()
    return render(request, "sell/new_book.html",
                  {'bookForm' : bookForm, 'itemForm': itemForm, 'authorForm': authorForm, 'publisherForm': publisherForm,
                  'isbn': isbn})

@login_required()
def newInventory(request):
    return render(request, 'sell/new_inventory.html', {})

@login_required()
def addNewBookPKCheck(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewBookISBNCheckForm(request.POST)
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
        form = NewBookISBNCheckForm()

    return render(request, "sell/new_book_isbn_check.html", {'isbnCheckForm': form})