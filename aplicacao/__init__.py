from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '48d3a419c01e4b01b3976596aefc278d'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///siteprodutos.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_maneger = LoginManager(app)
login_maneger.login_view = 'login'
login_maneger.login_message_category

from aplicacao import routers
