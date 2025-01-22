from flask import Blueprint, request, jsonify
import qrcode
import stripe
from models import User, Match, Booking, db
from utils import send_notification

booking_routes = Blueprint('booking', __name__)

# Payment gateway setup (Stripe)
stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'  # Replace with your Stripe test key

@booking_routes.route('/book', methods=['POST'])
def book_match():
    data = request.json
    user_id = data['user_id']
    match_id = data['match_id']
    payment_token = data['payment_token']

    # Process payment
    try:
        charge = stripe.Charge.create(
            amount=1000,  # Amount in cents (e.g., $10.00)
            currency='usd',
            source=payment_token,
            description='Match Booking'
        )
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 400

    # Save booking to database
    booking = Booking(user_id=user_id, match_id=match_id, qr_code=f"qrcodes/{user_id}_{match_id}.png")
    db.session.add(booking)
    db.session.commit()

    # Generate QR code
    qr = qrcode.make(f"BookingID:{booking.id}")
    qr.save(f"qrcodes/{user_id}_{match_id}.png")

    # Send notification
    send_notification(user_id, "Booking successful! Your QR code is ready.")

    return jsonify({"message": "Booking successful!", "qr_code": f"qrcodes/{user_id}_{match_id}.png"})

@booking_routes.route('/verify-qr', methods=['POST'])
def verify_qr():
    data = request.json
    qr_code = data['qr_code']

    # Check if QR code exists in the database
    booking = Booking.query.filter_by(qr_code=qr_code).first()
    if booking:
        return jsonify({"message": "QR code verified!", "valid": True})
    else:
        return jsonify({"message": "Invalid QR code.", "valid": False}), 400
