from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Car,User
from .forms import carForm, carChangeForm
from . import db
from flask_login import login_required, current_user


#create a blueprint
bp = Blueprint('cars', __name__, url_prefix='/cars')

@bp.route('/sold', methods = ['GET', 'POST'])
def sold():
  cars = Car.query.filter_by(sold='yes', user_id=current_user.name).all()  

  return render_template('cars/sold.html', cars=cars)


@bp.route('/create', methods = ['GET', 'POST'])
def create():
  form = carForm()
  print('Method type: ', request.method)
  if form.validate_on_submit():
    print('Successfully created new car', 'success')
    # access the values in the form data
    carlisting = Car(
                user_id=current_user.name,
                name=form.name.data, 
                minprice=form.minprice.data,
                odometer=form.odometer.data,
                description=form.description.data,
                image=form.image.data)
    # add the object to the db session
    db.session.add(carlisting)
    # commit to the database
    db.session.commit()
    
    return redirect(url_for('main.index'))

  return render_template('cars/create.html', form=form)


@bp.route('/edit/<id>', methods = ['GET', 'POST'])
def edit(id): 
  cars = Car.query.filter_by(id=id).first() 
  form = carChangeForm()

  print('Method type: ', request.method)
  if form.validate_on_submit():
    print('Successfully changed car details', 'success')
    # access the values in the form data
    cars.name=form.name.data
    cars.minprice=form.minprice.data
    cars.odometer=form.odometer.data
    cars.description=form.description.data
    cars.image=form.image.data
    cars.sold=form.sold.data

    db.session.add(cars)

    # commit to the database
    db.session.commit()
  
    return redirect(url_for('main.index'))

  return render_template('cars/edit.html', cars=cars, form=form)




    