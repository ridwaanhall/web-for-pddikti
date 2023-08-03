from flask import Flask

# Create the Flask app
app = Flask(__name__, instance_relative_config=True)

# Load configuration from the "config.py" file
app.config.from_object("config")

# Import routes to register them with the app
from app import routes
