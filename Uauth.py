###User Authentication (JWT + Password Hashing)

import bcrypt, jwt

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
    user = User(name=data['name'], email=data['email'], phone=data['phone'], password_hash=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return {'message': 'User registered successfully'}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.checkpw(data['password'].encode(), user.password_hash.encode()):
        token = jwt.encode({'user_id': user.id}, app.config['JWT_SECRET_KEY'], algorithm='HS256')
        return {'token': token}
    return {'error': 'Invalid credentials'}, 401
