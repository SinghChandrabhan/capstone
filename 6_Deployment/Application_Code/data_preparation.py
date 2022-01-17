import pandas as pd
from sklearn.preprocessing import StandardScaler

test_data = pd.read_csv("scenario1_test.csv")
test_data = test_data.drop(columns=['group','device_id']).dropna()
test_sample = test_data.sample(50)
age_sample = test_sample
gender_sample =test_sample

age_sample.gender = age_sample.gender.map(lambda x: 1 if x == "M" else 0)
age_sample = age_sample.drop(columns=['age'])


gender_sample = gender_sample.drop(columns='gender').dropna()
scaler = StandardScaler()
gender_sample_scaled =  scaler.fit(gender_sample).transform(gender_sample)
