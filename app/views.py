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

