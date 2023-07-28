from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log In")

app = Flask(__name__)
app.secret_key = "HELLO_WORLD"
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit() and request.method == "POST":
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
