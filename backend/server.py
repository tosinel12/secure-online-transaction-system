from flask import Flask, request, jsonify
from algorithm import SecureTransaction
import os

app = Flask(__name__)

# Initialize the secure transaction algorithm with a secret key
secret_key = os.urandom(32)
transaction = SecureTransaction(secret_key)

@app.route('/process_transaction', methods=['POST'])
def process_transaction():
    transaction_details = request.json

    # Validate the transaction details
    if not transaction.validate_transaction(transaction_details):
        return jsonify({'success': False, 'message': 'Invalid transaction details'}), 400

    # Encrypt the transaction details
    encrypted_transaction = transaction.encrypt_transaction(transaction_details)

    # Log the transaction details
    transaction.log_transaction(transaction_details)

    # Send a success response back to the front-end
    return jsonify({'success': True, 'encrypted_transaction': encrypted_transaction}), 200

if __name__ == '__main__':
    app.run(debug=True)
