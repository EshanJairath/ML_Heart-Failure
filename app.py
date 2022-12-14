
from flask import Flask, request ,render_template 
import pickle

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def home():
    model = pickle.load(open('rf_model.pkl', 'rb'))
    prediction=[]
    userInput = []
    result = "Enter Details And Click Submit"
    if request.method == 'POST' :
      
        age = request.form.get('age')
        age = float(age)
        userInput.append(age)

        anaemia = request.form.get('anaemia')
        anaemia = float(anaemia)
        userInput.append(anaemia)

        cpk = request.form.get('CPK')
        cpk = float(cpk)
        userInput.append(cpk)

        diabetes = request.form.get('diabetes')
        diabetes = float(diabetes)
        userInput.append(diabetes)

        ej_fra = request.form.get('ejection_fraction')
        ej_fra = float(ej_fra)
        userInput.append(ej_fra)

        highBP = request.form.get('highBP')
        highBP = float(highBP)
        userInput.append(highBP)

        platelets = request.form.get('platelets')
        platelets = float(platelets)
        userInput.append(platelets)

        ser_cre = request.form.get('Serum_creatinine')
        ser_cre = float(ser_cre)
        userInput.append(ser_cre)

        ser_sod = request.form.get('Serum_sodioum')
        ser_sod = float(ser_sod)
        userInput.append(ser_sod)
              
        sex = request.form.get('sex')
        sex = float(sex)
        userInput.append(sex)
        
        smoke = request.form.get('smoke')
        smoke = float(smoke)
        userInput.append(smoke)

        time = request.form.get('time')
        time = float(time)
        userInput.append(time)

        prediction = model.predict([userInput])
        # prediction = model.predict([[80,0,805,0,38,0,263358.03,1.1,134,1,0,109]]) 
        
        if prediction == [1]:
            result = "The patient is having a chance of heart failue"
        else:
            result = "The patient does not have a chance of heart failure"
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)