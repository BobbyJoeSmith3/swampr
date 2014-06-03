#====================================================
#views.py
#====================================================

#Allow for app to recognize and use characters from different languages
# -*- coding: utf-8 -*-

from app import app, db			#import our app and db components from other files
from flask import Flask, render_template, redirect
from models import Post, User
from forms import NewUserForm, NewPostForm

#This is the landing page

@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/landing_page')
def index():
	users = User.query.all()
	posts = Post.query.all()
	return render_template("landing_page.html", users = users, posts = posts)
	#This was from the first example
	#aliya_post_1 = Post("Not much to say", "Aliya", "Today was an unevetnful day")
	#we can just write "Post" because we imported the class Post from models
	#aliya_post_2 = Post("Today was a good day", "Aliya", "I don't know but today seems kinda odd. No barking from the dog. No smog. Had to stop at a red light. Looking in my mirror not a jacker in sight.")
	#maya_post_1 = Post("On History", "Dr. Angelou", "History, despite its wrenching pain, cannot be unlived, but if faced with courage, need not be lived again.")
	#return render_template('landing_page.html', posts = [aliya_post_1, aliya_post_2, maya_post_1])

@app.route('/add_user', methods = ['GET', 'POST'])
def add_user():
	form = NewUserForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/add_post')
	return render_template('add_user.html', form = form)

@app.route('/add_post', methods = ['GET', 'POST'])
def add_post():
	form = NewPostForm()
	if form.validate_on_submit():
		post = Post()
		form.populate_obj(post)
		db.session.add(post)
		db.session.commit()
		return redirect('/')
	return render_template('add_post.html', form = form)