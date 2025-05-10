
from flask import Flask, jsonify,request,render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
# Simulated queue system
queue = []
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/checkin', methods=['POST'])
def check_in():
    data = request.json
    name = data.get("name", "Unknown")
    checkin_time = datetime.now().strftime("%H:%M:%S")
    
    queue.append({"name": name, "checkin_time": checkin_time})
    
    return jsonify({"message": "Check-in successful!", "queue_position": len(queue)}), 200

@app.route('/queue', methods=['GET'])
def get_queue():
    return jsonify(queue), 200

@app.route('/next', methods=['POST'])
def next_patient():
    if queue:
        next_patient = queue.pop(0)
        return jsonify({"message": "Next patient called", "patient": next_patient}), 200
    return jsonify({"message": "Queue is empty"}), 400

if __name__ == '__main__':
    app.run(debug=True) 