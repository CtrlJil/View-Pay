## Create Database Models for storing user data 

#Create a class for user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

#Create a class for match
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(100))
    away_team = db.Column(db.String(100))
    match_time = db.Column(db.DateTime)

#Create a class for payments
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    amount = db.Column(db.Float)
    barcode = db.Column(db.String(255), unique=True)
    expiry_time = db.Column(db.DateTime)
