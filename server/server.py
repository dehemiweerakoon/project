from flask import  Flask,request,jsonify
from flask_cors import CORS
import  util
app = Flask(__name__)
CORS(app)

@app.route('/result',methods=['POST'])
def getresult():
    # current ->0
    # non-smoker-->1
    # past-smoker-->2

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

    risk_score = 0

    # Age factor
    if age >= 45:
        risk_score += 2

    # Blood glucose level factor
    if blood_glucose_level >= 126:
        risk_score += 3
    elif blood_glucose_level >= 100:
        risk_score += 1

    # BMI factor
    if bmi >= 30:
        risk_score += 2
    elif bmi >= 25:
        risk_score += 1

    # Smoking history factor
    if smoking_history == 2 | smoking_history==0:
        risk_score += 1

    # HbA1c level factor
    if HbA1c_level >= 6.5:
        risk_score += 3
    elif HbA1c_level >= 5.7:
        risk_score += 1

    # Hypertension factor
    if hypertension:
        risk_score += 2

    # Heart disease factor
    if heart_disease:
        risk_score += 2

    # Determine risk level (threshold can be adjusted)
    if risk_score >= 5:
        name= "high"
    else:
        name= "low"

    if result.item() ==1:
        name ="Cut down on free sugar wapping sugary drinks, energy drinks and fruit juices with water, plain milk, or tea and coffee without sugar can be a good start. Cutting out free sugars can help you manage your blood glucose levels and help you manage your weight."

    store_result = {  # Update global variable
        'result': result.item(),
        'statement': name
    }
    if(result.item()==1):
        ispositive ="Positive"
    else:
        ispositive ="Negative"
    response = jsonify({
        'result':ispositive,
        'statement':name
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response


if __name__ == "__main__":
    app.run()