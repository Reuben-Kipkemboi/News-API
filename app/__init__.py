from flask import Flask

from app.config import DevConfig

# Initializing our news application
app = Flask(__name__)

#setting up development configuration
app.config.from_object(DevConfig)


from app import views