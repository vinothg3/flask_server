from flask import Flask, request, jsonify
import jwt
from flask_cors import CORS

app = Flask(__name__)
secretKey = 'your_secret_key'  # Use the same secret key you used in the Node.js application
CORS(app)


@app.route('/receive_tokens', methods=['POST'])
def receive_tokens():
    data = request.get_json()
    print("hello")
    access_token = data.get('accessToken')
    refresh_token = data.get('refreshToken')
    
    # Process and use the received access and refresh tokens
    print('Received Access Token:', access_token)
    print('Received Refresh Token:', refresh_token)
    
    return 'Tokens received by Flask'

if __name__ == '__main__':
    app.run()
