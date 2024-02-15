from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db= SQLAlchemy() # IMPORT THE DATABASE
DB_NAME = "database.db" #define the name of the database
def create_app():
    app = Flask(__name__)  #initialize the app
    app.config["SECRET_KEY"] = "Mitsos" #confing with the secret key secures the cookies or the session data
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app) # initializing the database



    from . views import views # you import the blueprints
    from . auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import Note, User

    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):  # Fix the path separator and add the missing parenthesis
        with app.app_context():
            db.create_all()
        print('Created database!')