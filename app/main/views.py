from flask import render_template
from app import app
from..request import get_news, get_article

@app.route("/")
def home():
    """
    the home page being rendered by the render template
    
    """
    #Getting news from sources
    news_sources = get_news('sources')
    
    title = "welcome to Reuby News ---Todays insights"
    return render_template('index.html', title = title, sources=news_sources)

@app.route('/articles/<id>')
def articles(id):
    """_
    to display news and article details
    """
    articles = get_article(id)
    return render_template("news_details.html", id = id, articles =articles)

