from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)


class Car(db.Model):
    __tablename__ = 'carlisting'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80))
    name = db.Column(db.String(80))
    minprice = db.Column(db.Integer)
    odometer = db.Column(db.Integer)
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    sold = db.Column(db.String(3))
    user_id = db.Column(db.String(80))
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)
