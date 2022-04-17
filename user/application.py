from flask import Flask
from flask.sessions import SecureCookieSessionInterface
from flask_migrate import Migrate
from flask_login import LoginManager
#from models import db, User,init_app
import models 
from routes import user_blueprint

application = Flask(__name__)
application.config['SECRET_KEY'] = 'FmJ94aHQwIcNcvcoLu0B0A'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
application.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sumit2109@postgresscp.cytexzqgwbgc.us-east-1.rds.amazonaws.com/userscp'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

application.register_blueprint(user_blueprint)
models.init_app(application)
login_manager = LoginManager(application)
migrate = Migrate(application, models.db)


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    return None


class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""

    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5001)
