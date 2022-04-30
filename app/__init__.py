from flask import Flask

from app.config import DevConfig

# Initializing our news application
app = Flask(__name__,instance_relative_config = True) #connecting to instance folder when app is instantiated

#setting up development configuration
app.config.from_object(DevConfig)
# Getting our api instance folder to access our key
app.config.from_pyfile('config.py')


from app import views