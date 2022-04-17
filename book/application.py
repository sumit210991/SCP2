from flask import Flask
from routes import book_blueprint
from models import db, init_app
from flask_migrate import Migrate

application = Flask(__name__)
application.config['SECRET_KEY'] = '5fPxNUWP2Srzded6fayMeA'
#connection to the elib database.
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sumit2109@postgresscp.cytexzqgwbgc.us-east-1.rds.amazonaws.com/book'
#track modification turned off. 
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.register_blueprint(book_blueprint)
init_app(application)

migrate = Migrate(application, db)
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5002)
