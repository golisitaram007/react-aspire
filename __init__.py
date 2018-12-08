from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

root = os.path.join(os.path.dirname(os.path.abspath(__file__)))

@app.route("/")
def index():
    return send_from_directory(root, 'index.html')


# if __name__ == "__main__":
#     app.run()