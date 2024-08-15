"""Test configs."""
from app.app import create_app
from app.settings import ProdConfig, DevConfig


def test_production_config():
    """Production config."""
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'production'
    assert app.config['DEBUG'] is False


def test_dev_config():
    """Development config."""
    app = create_app(DevConfig)
    assert app.config['ENV'] == 'development'
    assert app.config['DEBUG'] is True