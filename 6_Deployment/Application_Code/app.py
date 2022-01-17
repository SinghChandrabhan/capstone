import data_preparation
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/predict')
def predict():
    age_model = pickle.load(
    open('age_prediction_model.sav', 'rb'))
    gender_model = pickle.load(
    open('gender_prediction_model.sav', 'rb'))
    age_predict = age_model.predict(data_preparation.age_sample)
    gender_predict = gender_model.predict(data_preparation.gender_sample_scaled)
    gender=[]
    age=[]
    val = []
    for i in range(0,49):
        gender.append(gender_predict[i])
        age.append(age_predict[i])

    '''
    Update the values of gender as M and F based on the cutoff value as LR predicts the probability.
    Here cutoff value derived during model building was : 
    '''    
    for i,j in enumerate(gender):
        if(j > 25):
            gender[i] = "M"
        else:
            gender[i] = "F"

    data = list(zip(gender,age))
    table_headings = ("Gender", "Age")

    return render_template('prediction.html', headings= table_headings, data = data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
