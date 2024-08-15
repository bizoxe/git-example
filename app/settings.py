"""Application configuration."""
import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'very-secret-key')
    LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT')

    SMTP_SERVER_NAME = os.getenv('SMTP_SERVER_NAME', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USER_PASSWORD = os.getenv('SMTP_USER_PASSWORD')
    SMTP_USER_LOGIN = os.getenv('SMTP_USER_LOGIN')
    MAIL_SENDER = os.getenv('MAIL_SENDER')
    MAIL_RECIPIENT = os.getenv('MAIL_RECIPIENT')
    MAIL_SUBJECT = os.getenv('MAIL_SUBJECT', 'Новый клиент!')


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'production'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False #for form validation