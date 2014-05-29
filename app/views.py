#====================================================
#views.py
#====================================================

#Allow for app to recognize and use characters from different languages
# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from models import Post

#This is the landing page

@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/landing_page')
def index():
	aliya_post_1 = Post("Not much to say", "Aliya", "Today was an unevetnful day")
	#we can just write "Post" because we imported the class Post from models
	aliya_post_2 = Post("Today was a good day", "Aliya", "I don't know but today seems kinda odd. No barking from the dog. No smog. Had to stop at a red light. Looking in my mirror not a jacker in sight.")
	maya_post_1 = Post("On History", "Dr. Angelou", "History, despite its wrenching pain, cannot be unlived, but if faced with courage, need not be lived again.")
	return render_template('landing_page.html', posts = [aliya_post_1, aliya_post_2, maya_post_1])
