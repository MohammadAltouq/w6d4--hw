from flask import Blueprint, render_template, redirect, request, url_for, flash
from drone_inventory.forms import UserLoginForm
from drone_inventory.models import User, db


auth = Blueprint('auth', __name__, template_folder= 'auth_templates')


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.first_name.data
            password = form.password.data

            user = User(email, password, first_name, last_name)

            db.session.add(user)
            db.session.commit()

            flash(f"You have succesfully created a user account {email}", "user-created")

            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please Check Your Form')
        
    return render_template('signup.html', form = form)

@auth.route('/signin')
def signin():
    return render_template('signin.html')

