#!/usr/bin/python3

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f2e815957e186cc01c6285b6293691a7'

posts = [
    {
        'author' : 'corey scwafer',
        'title' : 'blog post 1',
        'content' : 'first content',
        'date_posted' : 'april 1 2018'
    },
    {
        'author' : 'john doe',
        'title' : 'blog post 2',
        'content' : 'second content',
        'date_posted' : 'dec 12 2016'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts, title='alex')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)