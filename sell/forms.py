from django import forms
from store.models import BookStore, Item, Author, Publisher, Inventory
import autocomplete_light.shortcuts as autocomplete_light
from categories.category_helper import get_category_store_names, get_end_categories, get_store_end_categories
from accounts.models import Address
from django.core.exceptions import ObjectDoesNotExist

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        store = kwargs.pop('store', None)
        super(ItemForm, self).__init__(*args, **kwargs)
        category_choices = [(v, k) for k, v in get_store_end_categories(store).items()]
        self.fields['category'] = forms.MultipleChoiceField(label= "Select Categories", choices= category_choices)
    class Meta:
        model = Item
        exclude = ['posting_datetime', 'last_updated_datetime']

class StoreSelectForm(forms.Form):
    store_name_choices = [(k, k) for k, v in get_category_store_names()['store_names'].items()]
    store_names = forms.ChoiceField(label= "Select a store", choices= store_name_choices)

class NewBookForm(forms.ModelForm):

    class Meta(ItemForm.Meta):
        model = BookStore
        exclude = ['item', 'authors', 'publisher']

class NotLen13ISBNException(Exception):
    pass
class NewBookISBNCheckForm(forms.Form):

    isbn = forms.CharField(max_length= 13, min_length= 13, label= "ISBN", widget= forms.NumberInput())

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        try:
            if len(int(isbn)) != 13:
                raise NotLen13ISBNException
        except ValueError:
            self.add_error('isbn', "ISBN should be a number")
        except NotLen13ISBNException:
            self.add_error('isbn', "ISBN should be of length 13")
        return isbn

class NewBookAuthorForm(autocomplete_light.ModelForm):
    name = autocomplete_light.ModelMultipleChoiceField('AuthorAutocomplete', label = 'Author Name')
    class Meta:
        model = Author
        fields = ['name']

class NewBookPublisherForm(forms.ModelForm):
    name = autocomplete_light.ModelChoiceField('PublisherAutocomplete', label = 'Publisher Name')
    class Meta:
        model = Publisher
        fields = ['name']

class InventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['address'] = forms.ModelChoiceField(label= "Item Location",
                                                        queryset= Address.objects.filter(user= user))
    class Meta:
        model = Inventory
        exclude = ['item', 'seller', 'total_sold', 'currency', 'item_location', 'visibility', ]
        labels = {'condition': 'Item Condition', }
        help_texts = {'dispatch_max_time': 'In hours', }

class NewAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', ]

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Author.objects.get(name= name)
            self.add_error('name', "Author already present. No need to add the same name."
                                   "Use " + name + " in required field directly.")
        except ObjectDoesNotExist:
            return name

class NewPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', ]

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Publisher.objects.get(name= name)
            self.add_error('name', "Publisher already present. No need to add the same name."
                                   "Use " + name + " in required field directly.")
        except ObjectDoesNotExist:
            return name
