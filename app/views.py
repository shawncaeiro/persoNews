from flask import render_template, flash, redirect, session, url_for, request, g
from app import app
from .forms import SearchForm
import tweepy
from config import api

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        try: 
            tweets = api.user_timeline(screen_name = form.username.data, count = 50)
        except:
            flash("Username Error")
            return redirect(url_for('index'))
        tweetText = []
        for i in tweets:
            tweetText.append(i.text)
        session["user"] = form.username.data
        session["tweets"] = tweetText
        return redirect(url_for('results'))
    return render_template("index.html",
                           title='Home',
                           form= form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    name = session["user"]
    tweets = session["tweets"]
    return render_template("results.html",
                           name= name,
                           tweets = session["tweets"])

