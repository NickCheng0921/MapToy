from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS on all routes

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
