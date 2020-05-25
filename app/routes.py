from flask import render_template, redirect, flash
from app import App
from app.forms import LoginForm

# из папки app импортирую экземпляр класса Flask по имени App


@App.route('/')
@App.route('/index')
def index():
    words = ['привет', 'пока', 'я очень буду ждать звонка', 'полетели', 'hello']
    '''
        я связываю метку words на странице index.html
        со своим массивом words, в котором лежат слова
    '''
    return render_template('index.html', words=words)


@App.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)