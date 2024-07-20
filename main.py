from flask import Flask, request, jsonify, render_template, send_from_directory
from utils import pred_crop, pred_rainfall, pred_temp_hum

app = Flask(__name__)

# Define the directory where your static files (images) are stored
static_dir = "data/Crops"

# Route to serve static files (images)
@app.route('/static/Crops')
def serve_static(filename):
    return send_from_directory(static_dir, filename)

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('signup.html')
@app.route('/dashboard')
def dash():
    return render_template('index.html')



@app.route('/templates')
def login():
    return render_template('animated_login.html')

# Prediction endpoint
@app.route('/predict/', methods=['POST'])
def predict():
    data = request.get_json()
    nitrogen = data.get('nitrogen')
    phosphorous = data.get('phosphorous')
    potassium = data.get('potassium')
    state = data.get('state')
    district = data.get('district')
    month = data.get('month')
    ph = data.get('ph')
    
    try:
        rainfall = pred_rainfall.get_rainfall(state, district, month)
        temperature, humidity = pred_temp_hum.get_temp_hum(district)
        prediction = pred_crop.predict_crop(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall)
        return jsonify(result=prediction[0])
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
