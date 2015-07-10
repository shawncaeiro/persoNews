from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
import tweepy
from config import api

def isUsername(form):
    if form.username.data == "Shawn":
        raise ValidationError("No Shawns Allowed")

class SearchForm(Form):
    username = StringField('username', validators=[DataRequired()])