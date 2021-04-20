from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@myapp_obj.route('/', methods = ['GET', 'POST'])
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exits in database
        user = User.query.filter_by(author=form.author.data).first()
        # if not create user and add to database
        if user is None:
            user = User(author=form.author.data)
            db.session.add(user)
        # create row in Message table with user (created/found) add to ta database
        row = Messages(message = form.message.data, user_id = user.id)

    posts = [
        { 'author' : 'Carlos','message': 'Yo! Where you at?!'},
        { 'author':'Jerry', 'message':'Home. You?'}
        ]
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]

    return render_template('home.html', posts=posts, form=form)

