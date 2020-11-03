from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import  LoginManager
from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re 
import stripe

app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51HjRKQH7KlqUP8534T3z15yWA6P7ZRsaiUuNoidvGbbfVrZ1Pgjec44nWBI4CcrpK12q9m4PAn2OGMa27NwXDdOh00kmyM6vLa'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51HjRKQH7KlqUP853x0IoljLKMklujniwX4n9wCtVYX1qbNXxyXveIMRC4fVFVSVqMrc7fcaCFcmxO1qMXY9Crs2M00uPvPSBgO'

stripe.api_key = app.config['STRIPE_SECRET_KEY']
app.config.from_object('config')
db = MySQL(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)

from app.models import  forms
from  app.controllers import default
