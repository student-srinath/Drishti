from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_text = "Waiting for data..."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update_text():
    global latest_text
    latest_text = request.json.get("text", "")
    return jsonify({"status": "success", "received": latest_text})

@app.route('/get', methods=['GET'])
def get_text():
    return jsonify({"text": latest_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
