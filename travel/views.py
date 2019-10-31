from flask import Blueprint, render_template, request, session
from .models import Car

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')  # this is a decorator used in flask
def index():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)


@mainbp.route('/sell')  # this is a decorator used in flask
def sell():
    cars = Car.query.all()
    return render_template('Car Sell.html', cars=cars)

@mainbp.route('/bidform')
def bidform():
    return render_template('bidform.html')


#Pages
@mainbp.route('/High')
def High():
    return render_template('High-End.html')

@mainbp.route('/Medium')
def Medium():
    return render_template('Medium-End.html')

@mainbp.route('/Low')
def Low():
    return render_template('Low-End.html')

#Detail Pages
@mainbp.route('/Rolls')
def Rolls():
    return render_template('Rolls-Royce.html')

@mainbp.route('/Bentley')
def Bentley():
    return render_template('Bentley Continental.html')

@mainbp.route('/Ferrari')
def Ferrari():
    return render_template('Ferrari.html')

@mainbp.route('/Mercedes')
def Mercedes():
    return render_template('Mercedes-Benz.html')

@mainbp.route('/Audi')
def Audi():
    return render_template('Audi A3.html')

@mainbp.route('/Toyota')
def Toyota():
    return render_template('Toyota RAV4.html')

@mainbp.route('/Nissan')
def Nissan():
    return render_template('Nissan Pulsar.html')   

@mainbp.route('/Honda')
def Honda():
    return render_template('Honda Civic.html')   

@mainbp.route('/Suzuki')
def Suzuki():
    return render_template('Suzuki Swift.html')  

@mainbp.route('/Manage')
def Manage():
    return render_template('manageitems.html')  