from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourohfour(error):
    return render_template('errors/fourohfour.html')