#models.py

#class Post:
#	def __init__(self, title, author, content):			#The initialization method
#		self.title = title			#Defining the title attribute
#		self.author = author		#Defining the author attribute
#		self.content = content		#Defining the content attribute

from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(100))
	lastname = db.Column(db.String(100))
	username = db.Column(db.String(150), unique = True)
	#posts = db.relationship('Post', backref = 'author')		#allows us to refer to the table later without onerous select statements

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	author = db.Column(db.Integer, db.ForeignKey('user.id')) 		#user is referring to the class, and id is referring to the column being connected to.
	content = db.Column(db.Text)