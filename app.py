from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def home():
    return "Hi"
