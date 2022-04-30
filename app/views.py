from flask import render_template
from app import app

@app.route("/")
def home():
    """
    the home page being rendered by the render template
    
    """
    
    title = "welcome to Reuby News ---Todays insights"
    return render_template('index.html', title = title)

