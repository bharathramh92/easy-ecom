from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from helper import random_alphanumeric as ran
from django.core.mail import send_mail, EmailMessage
from easy_ecom import settings_sensitive
from django.contrib.auth.decorators import login_required
from .forms import StoreSelectForm, NewBookForm, NewBookISBNCheckForm, ItemForm, NewBookAuthorForm, \
    NewBookPublisherForm, InventoryForm, NewAuthorForm, NewPublisherForm
from accounts.forms import AddressForm
from store.models import BookStore, Item, Author, Publisher, Inventory
from django.core.exceptions import ObjectDoesNotExist
from helper import custom_http

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
    store_name = "Books"
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
        itemForm = ItemForm(request.POST, store=store_name)
        authorForm = NewBookAuthorForm(request.POST)
        publisherForm = NewBookPublisherForm(request.POST)
        # check whether it's valid:
        if bookForm.is_valid() and itemForm.is_valid() and authorForm.is_valid() and publisherForm.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            title = itemForm.cleaned_data['title']
            description = itemForm.cleaned_data['description']
            shipping_product_dimension_height = itemForm.cleaned_data['shipping_product_dimension_height']
            shipping_product_dimension_width = itemForm.cleaned_data['shipping_product_dimension_width']
            shipping_product_dimension_length = itemForm.cleaned_data['shipping_product_dimension_length']
            shipping_product_dimension_units = itemForm.cleaned_data['shipping_product_dimension_units']
            shipping_product_weight = itemForm.cleaned_data['shipping_product_weight']
            shipping_product_weight_units = itemForm.cleaned_data['shipping_product_weight_units']
            category = itemForm.cleaned_data['category']
            item = Item.objects.create(title= title, description= description, shipping_product_dimension_height= shipping_product_dimension_height,
                               shipping_product_dimension_width= shipping_product_dimension_width, shipping_product_dimension_length= shipping_product_dimension_length,
                               shipping_product_dimension_units= shipping_product_dimension_units, shipping_product_weight= shipping_product_weight,
                               shipping_product_weight_units= shipping_product_weight_units)
            item.category.add(*category)

            isbn_10 = bookForm.cleaned_data['isbn_10']
            isbn_13 = bookForm.cleaned_data['isbn_13']
            language = bookForm.cleaned_data['language']
            publisher = publisherForm.cleaned_data['name']

            book = BookStore.objects.create(isbn_10=isbn_10, isbn_13=isbn_13, language=language,
                                            item=item, publisher= publisher)
            authors = authorForm.cleaned_data['name']
            book.authors.add(*authors)

            return HttpResponseRedirect(reverse('sell:newInventory') + '?store_name=' + store_name + '&isbn_13=' + isbn_13)
    # if a GET (or any other method) we'll create a blank form
    else:
        bookForm = NewBookForm()
        itemForm = ItemForm(store="Books")
        authorForm = NewBookAuthorForm()
        publisherForm = NewBookPublisherForm()
    return render(request, "sell/new_book.html",
                  {'bookForm' : bookForm, 'itemForm': itemForm, 'authorForm': authorForm, 'publisherForm': publisherForm,
                  'isbn': isbn})

class StoreNotFoundException(Exception):
    pass

@login_required()
def newInventory(request):
    try:    #Proceed only if object exists for that store.
        store_name= request.GET['store_name']
        #retrieve item object as well
        if store_name == "Books":
            isbn_13 = request.GET['isbn_13']
            book = BookStore.objects.get(isbn_13=isbn_13)
            item = book.item
        else:
            raise StoreNotFoundException
        if len(Inventory.objects.filter(item = item, seller=request.user)) != 0:
            return render(request, 'sell/new_inventory_present_already.html', {})
    except (ObjectDoesNotExist, StoreNotFoundException) as e:
        print(e)
        raise PermissionDenied

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        inventoryForm = InventoryForm(request.POST, user= request.user.userextended)
        # check whether it's valid:
        if inventoryForm.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            price = inventoryForm.cleaned_data['price']
            # currency-->  # make a dict to map country and currency
            total_available_stock = inventoryForm.cleaned_data['total_available_stock']
            address = inventoryForm.cleaned_data['address']
            available_countries = inventoryForm.cleaned_data['available_countries']
            domestic_shipping_company = inventoryForm.cleaned_data['domestic_shipping_company']
            domestic_shipping_cost = inventoryForm.cleaned_data['domestic_shipping_cost']
            free_domestic_shipping = inventoryForm.cleaned_data['free_domestic_shipping']
            international_shipping_company = inventoryForm.cleaned_data['international_shipping_company']
            international_shipping_cost = inventoryForm.cleaned_data['international_shipping_cost']
            free_international_shipping = inventoryForm.cleaned_data['free_international_shipping']
            local_pick_up_accepted = inventoryForm.cleaned_data['local_pick_up_accepted']
            dispatch_max_time = inventoryForm.cleaned_data['dispatch_max_time']
            return_accepted = inventoryForm.cleaned_data['return_accepted']
            listing_end_datetime = inventoryForm.cleaned_data['listing_end_datetime']
            condition = inventoryForm.cleaned_data['condition']

            Inventory.objects.create(item=item, seller=request.user, price=price, total_available_stock= total_available_stock,
                                     item_location= address, available_countries= available_countries,
                                     domestic_shipping_company= domestic_shipping_company, domestic_shipping_cost= domestic_shipping_cost,
                                     free_domestic_shipping= free_domestic_shipping, international_shipping_company=international_shipping_company,
                                     free_international_shipping=free_international_shipping, local_pick_up_accepted= local_pick_up_accepted,
                                     dispatch_max_time= dispatch_max_time, return_accepted= return_accepted,
                                     listing_end_datetime= listing_end_datetime, condition= condition, international_shipping_cost=international_shipping_cost,

            )

            # redirect to item page:
            return render(request, 'sell/new_inventory_added.html', {})

    # if a GET (or any other method) we'll create a blank form
    else:
        inventoryForm = InventoryForm(user= request.user.userextended)
    return render(request, 'sell/new_inventory.html', {'inventoryForm': inventoryForm, 'get_params': custom_http.get_from_request_GET(request)})

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
                book = BookStore.objects.get(pk=isbn)
                #if found, redirect him to add as a seller in the listing
                get = '?store=Books&id=book.pk'
                return HttpResponse(reverse('sell:newInventory')+ get)
                # print("add him to the inventory")
            except Exception:
                #if not found, create a new book
                return HttpResponseRedirect(reverse('sell:newBook', kwargs= {'isbn' : isbn}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewBookISBNCheckForm()

    return render(request, "sell/new_book_isbn_check.html", {'isbnCheckForm': form})

@login_required()
def newAuthor(request):
    pass
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewAuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            Author.objects.create(name = name, created_by = request.user)
            return render(request, 'sell/new_author_added.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewAuthorForm()

    return render(request, 'sell/new_author.html', {'form': form})

@login_required()
def newPublisher(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewPublisherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            Publisher.objects.create(name = name, created_by = request.user)
            return render(request, 'sell/new_publisher_added.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewPublisherForm()

    return render(request, 'sell/new_publisher.html', {'form': form})