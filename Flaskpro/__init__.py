from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '3b4cbd3343b45e4150c291c33fb26190' #it was randomly created in python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_Manager = LoginManager(app)
login_Manager.login_view = 'login'
login_Manager.login_message_category = 'info'
from Flaskpro import routes