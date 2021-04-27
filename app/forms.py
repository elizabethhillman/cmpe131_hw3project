from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

'''this method creates a form for author, message and the submit button. gives parameters for string field to be required and the submit field to read Send''' 
class MessageForm(FlaskForm):
    # add
    # author (string) validator should make this textbox required
    author = StringField('Author', validators = [DataRequired()])
    # message (string) validator should make this textbox required
    message = StringField('Message', validators = [DataRequired()])
    # submit (button) text should say 'Send' 
    submit = SubmitField('Send')
