from app import app
from flask import render_template, request
from app.forms import searchForm
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="78b9d599c4f94f8fa3afb1a5458928d6")
#all routes get their respective news on call and render based on templates
@app.route("/search")
@app.route("/broken")
def broken():
    return render_template("broken.html")

@app.route("/search")
def search():
    form = searchForm(request.form)
    news = newsapi.get_everything(q=request.form['search']
                                ,language="en"
                                ,country="us")
    if news['status'] != 'ok':
        print("404 ERROR")
        return 
    return render_template('search.html', articles=news['articles'], form=form)

@app.route('/')
@app.route('/index')
def index():
    news = newsapi.get_top_headlines(category="technology",language="en")
    if news['status'] != 'ok':
        print("404 ERROR")
        return 
    return render_template('index.html', articles=news['articles'])

@app.route("/tech")
def tech():
    news = newsapi.get_top_headlines(category="technology"
                                    ,language="en"
                                    ,country="us")
    if news['status'] != 'ok':
        print("404 ERROR")
        return 

    return render_template('tech.html', articles = news['articles'])

@app.route("/entertainment")
def entertainment():
    news = newsapi.get_top_headlines(category="entertainment"
                                    ,language="en"
                                    ,country="us")
    if news['status'] != 'ok':
        print("404 ERROR")
        return 

    return render_template('entertainment.html', articles=news['articles'])

@app.route("/sports")
def sports():
    news = newsapi.get_top_headlines(category="sports"
                                    ,language="en"
                                    ,country="us")
    if news['status'] != 'ok':
        print("404 ERROR")
        return 

    return render_template('sports.html', articles=news['articles'])