"""The booking form module."""
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TimeField, TextAreaField
from wtforms.validators import DataRequired, Regexp


class BookingForm(FlaskForm):
    """Booking form."""

    name = StringField(
        validators=[
            DataRequired(message='* поле не должно быть пустым!'),
            Regexp(
                '^[а-яА-Я]*$',
                message='* имя должно содержать только символы а-я, А-Я.'
            ),
        ],
        render_kw={'placeholder': 'Имя *'},
    )
    phone = StringField(
        validators=[
            DataRequired(message='* поле не должно быть пустым!'),
        ],
        render_kw={'placeholder': 'Телефон *'},
    )
    services = SelectField(
        choices=[
            ('', 'Выберите услугу *'),
            ('повседневный макияж', 'повседневный макияж'),
            ('вечерний макияж', 'вечерний макияж'),
            ('лифтинг - макияж', 'лифтинг - макияж'),
            ('свадебный макияж', 'свадебный макияж'),
            ('для фотосессии', 'для фотосессии'),
            ('получить консультацию', 'получить консультацию')],
        validators=[
            DataRequired(message='* поле является обязательным!'),
        ],
    )
    date = DateField(label='Дата мероприятия:', default=datetime.now().date())
    time = TimeField(label='Время мероприятия:', default=datetime.now().time())
    message = TextAreaField(render_kw={'placeholder': 'Примечание к заказу (если необходимо):'})
