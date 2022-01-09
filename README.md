# capstone
Repo for machine learning capstone project 

Below are important links:

https://drive.google.com/drive/folders/1i1f5-kf1TV0dakD-JSVUHz2pZ_BnM8S9?usp=sharing
https://drive.google.com/drive/folders/1jMviLQm2i8n-3nNhV2JQHhYlS9VoRBJj?usp=sharing

https://www.meisterlabs.com/jobs/machine-learning-engineer/


C:\Users\chand\anaconda3\lib\site-packages\matplotlib\cbook\__init__.py


In this EDA we found that the prediction classes are unbalanced but they are representative of the chinese population where men are more and female are less and young people who use mobile phones are more than old people so we don't need to balance these classes using up sampling and downsampling, 

time based features are also explored the day of the week does not seem a good feature as the data for gender is similar for men and women but we can include it and see the performance, 
for hour based feature we can see it is a good feature as it varies considerably for different groups ,

Average number of events occuring each day is a feature we have created by feature engineering and does not seem like a good feature as the distribution is similar for men and women ,but don't know how it will perform on groups we can include it , 
we have created a feature median used time of day which also shows considerable variation on the group so it is a good feature, 
we have explored the labels feature and we can see that some labels have more men than women in them and the number of men and women vary considerably in these features so the labels is an important feature.We can create a bag of labels for each device as a feature, 
last we have analyzed the location feature and we have regions where only one type of groups exist so it is a good feature.

moment_feature





https://www.kaggle.com/kylingu/talkingdata-learning
https://www.kaggle.com/c/talkingdata-mobile-user-demographics/data?select=label_categories.csv.zip
https://medium.com/@rishabhbhatia315/talking-data-mobile-user-demographics-prediction-f0173a0577d2
https://github.com/cuckooinc/TalkingData-Mobile-User-Demographics/blob/master/All%20models.ipynb
https://github.com/cuckooinc/TalkingData-Mobile-User-Demographics/blob/master/EDA_TALKING_DATA.ipynb
https://www.kaggle.com/c/talkingdata-mobile-user-demographics/code?competitionId=5340&sortBy=voteCount&language=Python
https://www.kaggle.com/dvasyukova/brand-and-model-based-benchmarks
https://www.kaggle.com/beyondbeneath/geolocation-visualisations
