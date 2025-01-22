from flask import Flask, render_template
from models import Booking, db

app = Flask(view_pay)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/admin/dashboard')
def admin_dashboard():
    bookings = Booking.query.all()
    return render_template('dashboard.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
