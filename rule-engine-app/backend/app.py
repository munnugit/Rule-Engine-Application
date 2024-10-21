from flask import Flask
from routes import rule_blueprint
from database import init_db

app = Flask(__name__)

# Initialize the database
init_db()

# Register Blueprints
app.register_blueprint(rule_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
