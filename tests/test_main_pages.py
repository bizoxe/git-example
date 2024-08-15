"""The end-to-end tests for main pages routes module."""
import datetime

from flask import url_for
from werkzeug.datastructures import MultiDict

from app.main_pages.forms import BookingForm


def is_success_res(client, path):
    rv = client.get(path)
    assert rv.status_code == 200


def test_index_page(client):
    is_success_res(client, url_for('main_pages.index'))


def test_about_page(client):
    is_success_res(client, url_for('main_pages.about'))


def test_portfolio_page(client):
    is_success_res(client, url_for('main_pages.portfolio'))


def test_price_page(client):
    is_success_res(client, url_for('main_pages.price_page'))


def test_contact_page(client):
    """Booking form validation testing."""
    data = MultiDict(
        [
            ('name', 'Александр'),
            ('phone', '+375(25)-708-22-22'),
            ('services', 'лифтинг - макияж'),
            ('date', f'{datetime.datetime.now().date()}'),
            ('time', f'{datetime.datetime.now().strftime("%H:%M")}'),
            ('message', 'Need makeup by Thursday.'),
        ],
    )
    form = BookingForm(formdata=data)
    is_success_res(client, url_for('main_pages.contact_page'))
    response = client.post(url_for('main_pages.contact_page'), data=data)
    form.validate()
    assert form.validate() and response.status_code == 200
