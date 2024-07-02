import googlemaps
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
import os


# Initialize the Google Maps client with your API key
API_KEY = 'AIzaSyDqUQ612HWNtf4_NKSlY_OHhuSaU4uOGGk'
gmaps = googlemaps.Client(key=API_KEY)

class AddressCompleter(Completer):
    def get_completions(self, document, complete_event):
        if len(document.text) < 3:
            return
        
        query = document.text
        suggestions = get_place_suggestions(query)
        for suggestion in suggestions[:5]:
            yield Completion(suggestion['description'], start_position=-len(query))

def get_place_suggestions(query):
    response = gmaps.places_autocomplete(input_text=query)
    return response

def display_selected_address(address):
    print(f"\nYou selected: {address}")

if __name__ == "__main__":
    completer = AddressCompleter()
    address = prompt("Current Address: ", completer=completer)
    display_selected_address(address)
