from app import db

'''sets a colum for user data (id and the author name) in the db, links authors message to their name'''
class User(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key = True)
    # author (string, unique, can't be null)
    author = db.Column(db.String, nullable = False, unique = True)
    # message (linkd to Messages table)
    message = db.relationship('Messages', backref = 'User', lazy = 'dynamic')

    '''returns the author'''
    def __repr__(self):
        return '<User {}>'.format(self.author)

'''creates column for message data (id, message, & user_id) in db'''
class Messages(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key = True)
    # message (string, not unique, can't be null)
    message = db.Column(db.String, nullable = False, unique = False)
    # user_id link to id (int)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # write __repr__ that outputs
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message

    '''returns the message'''
    def __repr__(self):
        return '<Message: {}>'.format(self.body)
