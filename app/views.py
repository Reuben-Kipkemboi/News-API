from imp import source_from_cache
from flask import render_template
from app import app
from.request import get_news

@app.route("/")
def home():
    """
    the home page being rendered by the render template
    
    """
    #Getting news from sources
    news_sources = get_news('sources')
    
    title = "welcome to Reuby News ---Todays insights"
    return render_template('index.html', title = title, sources=news_sources)

@app.route('/news/<source_id>')
def news_details(source_id):
    """_
    to display news and article details
    """
    return render_template("news_details.html", id=source_id)

