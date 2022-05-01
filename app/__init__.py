from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
bootstrap = Bootstrap()

# Initializing our news application
def create_app(config_name):
    app = Flask(__name__) #connecting to instance folder when app is instantiated

#setting up development configuration
    app.config.from_object(config_options[config_name])
# Getting our api instance folder to access our key
   
    bootstrap.init_app(app)
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # setting config
    from .request import configure_request
    configure_request(app)
    return app