from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import booking_routes
from utils import send_notification

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Register routes
app.register_blueprint(booking_routes)

if __name__ == '__main__':
    app.run(debug=True)
