from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required
from car_inventory.models import db, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix = '/api')

# @api.route('getdata', methods= ['GET'])
@api.route('/getdata')
@token_required 
def getdata(our_user):
    return{'some': 'value'}

#creat Car endpoint

@api.route('/cars', methods = ['POST'])
@token_required
def create_car(our_user):
    # id = request.json['id']
    make = request.json['make']
    model = request.json['model']
    price = request.json['price']
    max_speed = request.json['max_speed']
    mpg = request.json['mpg']
    user_token = our_user.token
    print(f"user Token: {our_user.token})")

    car = Car( make, model, price, mpg, max_speed, user_token = user_token)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(our_user, id):
    owner = our_user.token
    if owner == our_user.token:
        car = Car.query.get(id)

        response = car_schema.dump(car)

        return jsonify(response)
    else:
        return jsonify({'message' : 'balid id Required'}), 401
    
@api.route('/cars/<id>' , methods = ['PUT', 'POST'])
@token_required
def update_car(our_user, id):
    car = Car.query.get(id)
    car.make = request.json['make']
    car.model = request.json['model']
    car.price = request.json['price']
    car.max_speed = request.json['max_speed']
    car.MPG = request.json['mpg']
    car.user_token = our_user.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# RETRIEVE ALL cars ENDPOINT
@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_cars(our_user, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)