#!/usr/bin/python3

import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""Main Flask application file"""

# Import the blueprint from the views module
from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from os import getenv
from models import storage

# Create a new Flask app instance
app = Flask(__name__)

# Register the blueprint with the app
app.register_blueprint(app_views)

# Define a function to clean up the database session after each request
@app.teardown_appcontext
def clean_up(exception=None):
    """Eliminates current database session"""
    storage.close()

# Define an error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    """Handles 404 error"""
    return jsonify({"error": "Not found"}), 404

# Define the main entry point for the application
if __name__ == "__main__":
    # Get the host and port from environment variables, or use defaults
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    # Start the app on the specified host and port
    app.run(host, int(port), threaded=True)

