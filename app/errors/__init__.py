"""The error's module."""
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers