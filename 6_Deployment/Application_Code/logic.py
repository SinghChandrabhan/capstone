import imp
import pickle
import data_preparation
from decimal import Decimal

"""This file contains logic to get the prediction from model and merge the lists"""

def predict():
    age_model = pickle.load(open('age_prediction_model.pkl', 'rb'))
    gender_model = pickle.load(open('gender_prediction_model.pkl', 'rb'))
    age_predict = age_model.predict(data_preparation.age_sample)
    gender_predict = gender_model.predict(data_preparation.gender_sample_scaled)
    gender_predict_prob = gender_model.predict_proba(data_preparation.gender_sample_scaled)
    gender=[]
    age=[]
    gender_prob = []
    for i in range(0,49):
        gender.append(gender_predict[i])
        gender_prob.append(Decimal(float(gender_predict_prob[i][1])))
        age.append(age_predict[i])
    return data_preparation.device_id,gender,gender_prob,age

#used to merge 3 uneven list
def mergelist(list1, list2, list3):
    merged_list = []
    l1 = len(list1)
    l2 = len(list2)
    l3 = len(list3)
    for i in range(max(l1,l2,l3)):
        while True:
            try:
                tup = (list1[i], list2[i], list3[i])
            except IndexError:
                if (l1>l2) and (l1>l3):
                    list2.append('')
                    list3.append('')
                    tup = (list1[i], list2[i], list3[i])
                elif (l2>l1) and (l2 > l3):
                    list1.append('')
                    list3.append('')
                    tup = (list1[i], list2[i], list3[i])
                elif (l3>l1) and (l3 > l2):
                    list1.append('')
                    list3.append('')
                    tup = (list1[i], list2[i], list3[i])
                continue
            merged_list.append(tup)
            break
    return merged_list

#used to merge 2 uneven list
def merge2list(list1, list2):
    merged_list = []
    l1 = len(list1)
    l2 = len(list2)
    for i in range(max(l1,l2)):
        while True:
            try:
                tup = (list1[i], list1[i], list2[i])
            except IndexError:
                if l1>l2:
                    list2.append('')
                    tup = (list1[i], list1[i], list2[i])
                elif l2>l1 :
                    list1.append('')
                    tup = (list1[i], list1[i], list2[i])
                continue
            merged_list.append(tup)
            break
    return merged_list