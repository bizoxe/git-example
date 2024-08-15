"""Defines fixtures available to all tests."""
import pytest

from app.app import create_app
from app.settings import TestingConfig


@pytest.fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestingConfig)
    _app.config['SMTP_SERVER_NAME'] = 'smtp.gmail.com'
    _app.config['SMTP_PORT'] = 587
    _app.config['SMTP_USER_LOGIN'] = 'matveevalexander79@gmail.com'
    _app.config['SMTP_USER_PASSWORD'] = 'pzkaomjkkwqblcsz'
    _app.config['MAIL_SENDER'] = 'matveevalexander79@gmail.com'
    _app.config['MAIL_RECIPIENT'] = 'dolgorukaya.makeaup@gmail.com'
    _app.config['MAIL_SUBJECT'] = 'Новый клиент!'

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture()
def client(app):
    """Creates a test client for application."""
    return app.test_client()


