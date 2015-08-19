from django import forms
from store.models import BookStore, StoreName, Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

class StoreSelectForm(forms.Form):

    store_name_choices = [(x.store_name, x.store_name) for x in StoreName.objects.all()]
    store_names = forms.ChoiceField(label= "Select a store", choices= store_name_choices)

class NewBookForm(forms.ModelForm):

    class Meta(ItemForm.Meta):
        model = BookStore
        exclude = ['item']

class ISBNCheckForm(forms.Form):

    isbn = forms.CharField(max_length= 13, min_length= 13, label= "ISBN", widget= forms.NumberInput())

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        try:
            int(isbn)
        except Exception:
            self.add_error('isbn', "ISBN should be a number")
        return isbn
