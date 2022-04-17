from flask import Flask
from routes import emailexcel_blueprint

application=Flask(__name__)
application.register_blueprint(emailexcel_blueprint)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)