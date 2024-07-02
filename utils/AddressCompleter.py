import googlemaps
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion

class AddressCompleter(Completer):
    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)
        self.prompt = prompt

    def get_place_suggestions(self, query):
        response = self.gmaps.places_autocomplete(input_text=query)
        return response

    def display_selected_address(address):
        print(f"\nYou selected: {address}")

    def get_completions(self, document, complete_event):
        if len(document.text) < 3:
            return
        
        query = document.text
        suggestions = self.get_place_suggestions(query)
        for suggestion in suggestions[:5]:
            yield Completion(suggestion['description'], start_position=-len(query))
