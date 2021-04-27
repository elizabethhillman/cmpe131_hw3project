from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

'''routes the webpage to the message form'''
# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods = ['GET', 'POST'])
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        '''checks db by authors name to see if they exist or not'''
        user = User.query.filter_by(author=form.author.data).first()
        # if not create user and add to database
        if user is None:
            '''creates user and adds them to db'''
            user = User(author=form.author.data)
            db.session.add(user)
            db.session.commit()
        # create row in Message table with user (created/found) add to ta database
            '''creates row based on user id'''
            row = Messages(message = form.message.data, user_id = user.id)
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

    '''saves all messages in a variable to be used later'''
    messages = Messages.query.all()
    '''for all the messages that have been posted, adds them to dictionary and is visible to user'''
    for currentMessage in messages:
        posts = posts + [
            { 'author' : User.query.filter_by(id=currentMessage.id).first().author, 'message' : currentMessage.message}]     

    return render_template('home.html', posts=posts, form=form)

