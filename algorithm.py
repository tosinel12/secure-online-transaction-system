import hashlib
import hmac
import os

class SecureTransaction:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt_transaction(self, transaction_details):
        # Encrypt transaction details using HMAC with SHA-256
        transaction_string = str(transaction_details).encode('utf-8')
        encrypted_transaction = hmac.new(self.secret_key, transaction_string, hashlib.sha256).hexdigest()
        return encrypted_transaction

    def authenticate_user(self, user_id, user_token):
        # Authenticate user by comparing provided token with stored token
        stored_token = self.get_stored_token(user_id)
        return hmac.compare_digest(stored_token, user_token)

    def validate_transaction(self, transaction_details):
        # Validate transaction details (e.g., check for required fields)
        required_fields = ['amount', 'currency', 'recipient']
        for field in required_fields:
            if field not in transaction_details:
                return False
        return True

    def log_transaction(self, transaction_details):
        # Log transaction details for auditing and monitoring purposes
        with open('transaction_log.txt', 'a') as log_file:
            log_file.write(str(transaction_details) + '\n')

    def get_stored_token(self, user_id):
        # Retrieve stored token for the given user ID (dummy implementation)
        return 'stored_token_for_user_' + str(user_id)

# Example usage
if __name__ == "__main__":
    secret_key = os.urandom(32)
    transaction = SecureTransaction(secret_key)

    transaction_details = {
        'amount': 100,
        'currency': 'USD',
        'recipient': 'recipient@example.com'
    }

    if transaction.validate_transaction(transaction_details):
        encrypted_transaction = transaction.encrypt_transaction(transaction_details)
        print("Encrypted Transaction:", encrypted_transaction)
        transaction.log_transaction(transaction_details)
    else:
        print("Invalid transaction details")
