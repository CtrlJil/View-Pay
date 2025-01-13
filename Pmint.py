### ** Payment Integration (Flutterwave)**

from rave_python import Rave
rave = Rave("PUBLIC_KEY", "SECRET_KEY", production=False)

@app.route('/pay', methods=['POST'])
def process_payment():
    data = request.get_json()
    payment = rave.Card.charge({
        "cardno": data['card_number'],
        "cvv": data['cvv'],
        "expirymonth": data['exp_month'],
        "expiryyear": data['exp_year'],
        "amount": data['amount'],
        "email": data['email'],
        "phonenumber": data['phone'],
        "currency": "USD"
    })
    if payment["status"] == "success":
        return {'message': 'Payment successful'}
    return {'error': 'Payment failed'}, 400
