from flask import Blueprint, render_template, request, redirect,url_for
from flask_login import login_required, current_user
from car_inventory.forms import CarForm
from car_inventory.models import Car, db

site = Blueprint('site', __name__ , template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')
@site.route('/profile', methods =['GET', 'POST'])
@login_required
def profile():
    my_car = CarForm()
    try:
        if request.method == 'POST' and my_car.validate_on_submit():
            make = my_car.make.data
            model = my_car.model.data
            price = my_car.price.data
            max_speed = my_car.max_speed.data
            mpg = my_car.mpg.data
            user_token = current_user.token
            car = Car(make, model,price , max_speed, mpg, user_token)

            db.session.add(car)
            db.session.commit()
            return redirect(url_for('site.profile'))
    
    except:
        raise Exception('Car not created, please check your form and try again!')

    user_token = current_user.token
    cars = Car.query.filter_by(user_token = user_token)
    return render_template('profile.html', form = my_car, cars = cars)



