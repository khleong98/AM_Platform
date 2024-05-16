import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from models import db
from routes import blueprint


BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder='static')

app.config['BASE_DIR'] = BASE_DIRECTORY
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIRECTORY, 'am_platform.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(blueprint)

CORS(app, origins=['http://localhost:8080'])

db.init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)