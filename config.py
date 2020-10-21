import os.path
basedir = os.path.abspath(os.path.dirname(__file__))
Debug= True
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS= True

SECRET_KEY = '1235789aAsd!' 
MAIL_SERVER= "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'emersonsf.info@gmail.com'
MAIL_PASSWORD = 'kezkxirfaqkrjiis'
