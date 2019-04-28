# auth's __init__.py file
from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views