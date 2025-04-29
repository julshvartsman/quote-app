
"""
app.py - Flask backend for the Quote of the Day app
"""
from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
# Enable CORS for all routes to allow requests from your frontend
CORS(app)

# Sample quotes
quotes = [
    {
        "text": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon"
    },
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    },
    {
        "text": "In the end, it's not the years in your life that count. It's the life in your years.",
        "author": "Abraham Lincoln"
    },
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt"
    },
    {
        "text": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "author": "Winston Churchill"
    },
    {
        "text": "The best way to predict the future is to create it.",
        "author": "Peter Drucker"
    },
    {
        "text": "The purpose of our lives is to be happy.",
        "author": "Dalai Lama"
    },
    {
        "text": "You only live once, but if you do it right, once is enough.",
        "author": "Mae West"
    },
    {
        "text": "Be yourself; everyone else is already taken.",
        "author": "Oscar Wilde"
    },
    {
        "text": "The journey of a thousand miles begins with one step.",
        "author": "Lao Tzu"
    }
]

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    """Return a random quote from our collection"""
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

@app.route('/', methods=['GET'])
def index():
    """Simple index route to check if API is running"""
    return jsonify({
        "message": "Quote API is running!",
        "endpoints": {
            "/api/quote": "Get a random quote"
        }
    })

if __name__ == '__main__':
    # Get port from environment variable (useful for deployment) or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    # Run the app with the host set to '0.0.0.0' to make it publicly accessible
    app.run(host='0.0.0.0', port=port, debug=True)