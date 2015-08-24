import autocomplete_light.shortcuts as autocomplete_light
from store.models import Author

class AuthorAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name']
    model = Author

autocomplete_light.register(AuthorAutocomplete)