import pandas as pd
from sklearn.preprocessing import StandardScaler

'''Initial data preperation i.e to get the smaple of 50 records from test file'''

''' scenario1_test.csv will generate at end of model building and be placed in in Application code.
Alternately it can also be downloaded from S3: https://upgradcapstone.s3.amazonaws.com/test-data/scenario1_test.csv'''

test_data = pd.read_csv("scenario1_test.csv")
test_data = test_data.dropna()
test_sample = test_data.sample(50)
device_id = test_sample['device_id'].tolist()

age_sample = test_sample
gender_sample =test_sample


age_sample.gender = age_sample.gender.map(lambda x: 1 if x == "M" else 0)
age_sample = age_sample.drop(columns=['age', 'group', 'device_id'])


gender_sample = gender_sample.drop(columns=['gender','group', 'device_id'])
scaler = StandardScaler()
gender_sample_scaled =  scaler.fit(gender_sample).transform(gender_sample)
