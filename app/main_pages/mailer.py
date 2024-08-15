"""The email server module."""
from datetime import datetime
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import current_app


def booking_message(form, mail_subject, mail_from, mail_to) -> 'html':
    """Creates a booking message."""
    mail = MIMEMultipart('alternative')
    mail['Subject'] = mail_subject
    mail['From'] = mail_from
    mail['To'] = mail_to
    data = form.data
    data.pop('csrf_token', None)
    if data['date'] == datetime.now().date() and data['time'].strftime('%H') == datetime.now().strftime('%H'):
        data['date'] = 'не задано'
        data['time'] = 'не задано'
    date = str(data.pop('date'))
    time = str(data.pop('time'))
    data.update(date=date, time=time)
    msg = '<html><head></head><body>'
    for key, value in data.items():
        msg += key + " : " + value + '<br>'
        msg += '</body></html>'
    mail.attach(MIMEText(msg, 'html'))
    return mail

def email_server(form) -> None:
    """Sends a message to the customer's e-mail account."""
    host = current_app.config.get('SMTP_SERVER_NAME')
    port = current_app.config.get('SMTP_PORT')
    user_login = current_app.config.get('SMTP_USER_LOGIN')
    password = current_app.config.get('SMTP_USER_PASSWORD')
    mail_subject = current_app.config.get('MAIL_SUBJECT')
    mail_from = user_login
    mail_to = current_app.config.get('MAIL_RECIPIENT')
    message = booking_message(form=form,
                              mail_subject=mail_subject,
                              mail_from=mail_from,
                              mail_to=mail_to,)
    context = ssl.create_default_context()
    with smtplib.SMTP(host=host, port=port) as server:
        server.starttls(context=context)
        server.login(user_login, password)
        try:
            server.sendmail(mail_from, mail_to, message.as_string())
            current_app.logger.info('Successfully result was sent to the recipient email.')
        except smtplib.SMTPResponseException as error:
            error_code = error.smtp_code
            error_message = error.smtp_error
            current_app.logger.error(f'Observed exception while send email to recipient email!,\n'
                                     f'Exception: {error_message}, {error_code}')
        except smtplib.SMTPException as error:
            current_app.logger.error(f'Observed exception while send email to recipient email!,\n'
                                     f'Exception: {error}')







