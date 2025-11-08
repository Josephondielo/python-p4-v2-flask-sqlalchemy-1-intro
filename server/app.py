from flask import Flask
from flask_migrate import Migrate

from models import db  # import SQLAlchemy instance and models

# create a Flask application object
app = Flask(__name__)

# configure a database connection to a local SQLite file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema migrations
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

# optional: add a simple test route
@app.route('/')
def index():
    return "Flask app with SQLAlchemy and Migrate is running!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
