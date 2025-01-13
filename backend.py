### Setting Up the Backend
 from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_jwt_extended import JWTManager

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/football_center'
   app.config['JWT_SECRET_KEY'] = 'supersecurekey'
   db = SQLAlchemy(app)
   jwt = JWTManager(app)
