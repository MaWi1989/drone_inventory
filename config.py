import os
from dotenv import load_dotenv

basedir =os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """set configuration variables for flak app
    using environment variables where available
    otherwise create config variable if not done already"""


    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get("SECRET_KEY") or "You'll never guess!"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite://" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #turns of messages from sqlalchemy regarding updates to our db



