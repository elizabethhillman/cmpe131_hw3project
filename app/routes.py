from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods = ['GET', 'POST'])
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        user = User.query.filter_by(author=form.author.data).first()
        # if not create user and add to database
        if user is None:
            user = User(author=form.author.data)
            db.session.add(user)
            db.session.commit()
        # create row in Message table with user (created/found) add to ta database
            row = Messages(message = form.message.data, user_id = User.query.filter_by(author=form.author.data).first().id)
            db.session.add(row)
            db.session.commit()

    posts = [
        { 'author' : 'Carlos','message': 'Yo! Where you at?!'},
        { 'author':'Jerry', 'message':'Home. You?'}
        ]
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]

    messages = Messages.query.all()
    for currentMessage in messages:
        posts = posts + [
            { 'author' : User.query.filter_by(id=currentMessage.id).first().author},{ 'message' : currentMessage.message}]     

    return render_template('home.html', posts=posts, form=form)

