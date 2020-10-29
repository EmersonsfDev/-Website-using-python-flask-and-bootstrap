from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import  LoginManager
from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re 

app = Flask(__name__)

app.config.from_object('config')
db = MySQL(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)

from app.models import  forms
from  app.controllers import default
