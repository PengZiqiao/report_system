from flask import Blueprint

weekly = Blueprint('weekly', __name__, url_prefix='/weekly')

from . import views
