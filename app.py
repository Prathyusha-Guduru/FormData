from flask import Flask,render_template,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email
from wtforms import ValidationError


#########################################
################## CONFIG    ############
#########################################


app = Flask(__name__)
app.config['SECRET_KEY'] = 'izzasecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)


#########################################
################## DB MODELS ############
#########################################
class Waitlist(db.Model):
	__tablename__ = 'waitlist'

	id = db.Column(db.Integer,primary_key = True)
	email = db.Column(db.String(64),unique = True,index = True)
	firstname = db.Column(db.String(64),index = True)
	lastname = db.Column(db.String(64),index = True)


	def __init__(self,email,firstname,lastname):
		self.email = email
		self.firstname= firstname
		self.lastname = lastname



	def __repr__(self):
		return f"name is {self.firstname} {self.lastname}, email is {self.email}"

#########################################
################## FORMS ################
#########################################


class WaitListForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	firstname = StringField('firstname',validators=[DataRequired()])
	lastname = StringField('lastname',validators=[DataRequired()])
	
	submit = SubmitField('Submit')

	def check_email(self,field):
		if Waitlist.query.filter_by(email = field.data).first():
			return True
#########################################
################## VIEWS ################
#########################################

@app.route('/',methods = ['GET','POST'])
def index():
	form = WaitListForm()
	if form.validate_on_submit():
		if(form.check_email(form.email)):
			flash("Email already registered")
		else:

			newJoin = Waitlist(email=form.email.data,firstname = form.firstname.data, lastname = form.lastname.data)
			db.session.add(newJoin)
			db.session.commit()
			flash("Succesfull!","info")
	return render_template('index.html',form = form)



if __name__ == "__main__":
	app.run(debug = True)
