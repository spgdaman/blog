from flask import render_template, flash, abort, request, url_for, redirect
from ..requests import get_random_quote

@main.route('/random_quote')
def show_quote():
    quote = get_random_quote()
    return redirect('quotes.html',quotes=quote)