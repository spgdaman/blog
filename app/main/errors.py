from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourohfour():
    return render_template('errors/fourohfour.html')