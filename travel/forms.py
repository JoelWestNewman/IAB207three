from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class carForm(FlaskForm):
  name = StringField('Car Name', validators=[InputRequired()])
  minprice = StringField('Minimum Sell Price', validators=[InputRequired()])
  odometer = StringField('Odometer', validators=[InputRequired()])
  description = TextAreaField('Description of the Car', 
            validators=[InputRequired(), Length(min=10, max=200)])
  image = StringField('Car Image', validators=[InputRequired()])
  submit = SubmitField("Submit")


class carChangeForm(FlaskForm):
  name = StringField('Car Name', validators=[InputRequired()])
  minprice = StringField('Minimum Sell Price', validators=[InputRequired()])
  odometer = StringField('Odometer', validators=[InputRequired()])
  description = TextAreaField('Description of the Car', 
            validators=[InputRequired(), Length(min=10, max=200)])
  image = StringField('Car Image', validators=[InputRequired()])
  sold = StringField('Sold Value', validators=[InputRequired()])
  submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")