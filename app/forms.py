from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required
#you will need to type in "pip install flask-wtf" in a new virtual environment

class NewUserForm(Form):
	firstname = TextField('firstname')
	lastname = TextField('lastname')
	username = TextField('username', validators = [Required()])

class NewPostForm(Form):
	title = TextField('title', validators = [Required()])
	content = TextAreaField('content', validators = [Required()])