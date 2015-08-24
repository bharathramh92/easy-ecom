import autocomplete_light.shortcuts as autocomplete_light
from store.models import Author, Publisher

autocomplete_light.register(Author,
    search_fields = ['^name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Add Authors',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
)

autocomplete_light.register(Publisher,
    search_fields = ['^name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Add Publisher',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
)