from flask import render_template,request,redirect, url_for
from . import main
from..request import get_news, get_article

@main.route("/")
def home():
    """
    the home page being rendered by the render template
    
    """
    #Getting news from sources
    news_sources = get_news('sources')
    
    title = "welcome to Reuby News ---Todays insights"
    return render_template('index.html', title = title, sources=news_sources)

@main.route('/articles/<id>')
def articles(id):
    """_
    to display news and article details
    """
    articles = get_article(id)
    return render_template("news_details.html", id = id, articles =articles)

