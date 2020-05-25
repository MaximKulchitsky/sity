from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Ник', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    rememberMe = BooleanField('Запомнить вас?')
    submit = SubmitField('Войти')

