from crypt import methods
from heapq import merge
from flask import Flask, request, render_template, jsonify
import logic
from decimal import Decimal

'''This is the flask file to route application and display model'''

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def user_demographics():
    device_id, gender, gender_prob, age = logic.predict()
    for i,j in enumerate(gender):
        if j == 1: #since we have defined 1 as Male and 0 as female in model
            gender[i] = "M"
        else:
            gender[i] = "F" 
    data = list(zip(device_id, gender, age))
    table_headings = ("Device ID","Gender", "Age")
    return render_template('index.html', headings= table_headings, data = data)

@app.route('/age_campaign', methods = ['POST'])
def age_campaign():
    device_id, gender, gender_prob, age = logic.predict()
    age_bucket1 = []
    age_bucket2 = []
    age_bucket3 = []
    for i,j in enumerate(age):
        if j <= 24:
            age_bucket1.append(device_id[i])
        elif j>24 and j<=32:
            age_bucket2.append(device_id[i])
        else:
            age_bucket3.append(device_id[i])
    data = tuple(logic.mergelist(age_bucket1,age_bucket2,age_bucket3))
    table_headings = ("Campaign 4:Age Bucket(0-24)","Campaign 5:Age Bucket(24-32)", "Campaign 6:Age Bucket(32+)") #Lower limit is ignored
    return render_template('index.html', headings= table_headings, data = data)

@app.route('/gender_campaign', methods = ['POST'])
def gender_campaign():
    device_id, gender, gender_prob, age = logic.predict()
    max_prob = Decimal(0.79)
    min_prob = Decimal(0.54)
    campaign12 = []
    campaign3= []
    for i,j in enumerate(gender_prob):
        if j.compare(max_prob) == 1 or j.compare(max_prob) == 0:
            campaign3.append(device_id[i])
        elif j.compare(min_prob) == -1 or j.compare(min_prob) == 0:
            campaign12.append(device_id[i])
    data = tuple(logic.merge2list(campaign12,campaign3))
    table_headings = ("Campaign 1(Females)","Campaign 2(Females)", "Campaign 3(Males)")
    return render_template('index.html', headings= table_headings, data = data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
