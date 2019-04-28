import requests
from .models import Quotes

api_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_random_quote():
    response = requests.get(api_url)

    if response.status_code == 200:
        data=response.json()

        author = data.get('author')
        id = data.get('id')
        quote = data.get('quote')
        url = data.get('permalink')
        quote = Quotes(author,id,quote,url)
        return quote
    return False