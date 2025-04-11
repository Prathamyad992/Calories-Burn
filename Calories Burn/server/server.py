from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/predict_calorie', methods=['POST','GET'])
def predict_calorie():
    gender = float(request.form['gender'])
    age = request.form['age']
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    duration = request.form['duration']
    heart_rate = request.form['heart_rate']
    body_temp = request.form['body_temp']

    response = jsonify({
        'estimated_calorie': util.get_calorie(gender,age,height,weight,duration,heart_rate,body_temp)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Calorie Prediction...")
    util.load_saved_artifacts()
    app.run()