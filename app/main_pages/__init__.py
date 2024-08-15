"""The main_pages module."""
from flask import Blueprint

bp = Blueprint('main_pages', __name__)

from app.main_pages import routes