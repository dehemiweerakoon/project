from flask import  Flask,request,jsonify
import  util
app = Flask(__name__)

@app.route('/result',methods=['POST'])
def getresult():
    #hello

    data = request.get_json()
    gender = data.get('gender')
    age = data.get('age')
    hypertension = data.get('hypertension')
    heart_disease = data.get('heart_disease')
    smoking_history = data.get('smoking_history')
    bmi = data.get('bmi')
    HbA1c_level = data.get('HbA1c_level')
    blood_glucose_level = data.get('blood_glucose_level')
    result =util.get_result(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level)

    response = jsonify({
        'result':result.item()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response



if __name__ == "__main__":
    app.run()