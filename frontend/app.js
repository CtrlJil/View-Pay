import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [qrCode, setQrCode] = useState('');

    const handleBooking = async () => {
        const paymentToken = 'tok_visa';  // Replace with actual payment token
        const response = await axios.post('/book', {
            user_id: 1,
            match_id: 101,
            payment_token: paymentToken
        });
        setQrCode(response.data.qr_code);
    };

    return (
        <div>
            <h1>Book a Match</h1>
            <button onClick={handleBooking}>Book Now</button>
            {qrCode && <img src={qrCode} alt="QR Code" />}
        </div>
    );
}

export default App;
