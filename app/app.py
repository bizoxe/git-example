"""The app module, containing the app factory function."""
import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask

from app.settings import ProdConfig


def create_app(config_object=ProdConfig) -> Flask:
    """An application factory.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)

    from app.errors import bp as bp_errors
    app.register_blueprint(bp_errors)

    from app.main_pages import bp as bp_main_pages
    app.register_blueprint(bp_main_pages)

    from app.blog import bp as bp_blog
    app.register_blueprint(bp_blog)

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/makeup_art_web.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Website startup')

    return app