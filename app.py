from flask import Flask
from routes.analyze import analyze_bp

app = Flask(__name__)

app.register_blueprint(analyze_bp)

@app.route("/")
def home():
    return {
        "message": "Phishing Detection API is running!"
    }

if __name__ == "__main__":
    app.run(debug=True)