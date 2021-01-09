from flask import  render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
	user = {'username': 'Sartaj'}

	posts = [{"author": {"username": "John"},
    	          "body": "A Beautiful Day in Bangalore."},
	         {"author": {"username": "Susan"},
	          "body": "The Avengers was a good movie."},
	         {"author": {"username": "Donald Glover"},
	          "body": "It feels like summer!"}]

	return render_template("index.html", user=user, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))

	return render_template('login.html', title='Sign In', form=form)


if 0:
    print(1234)


