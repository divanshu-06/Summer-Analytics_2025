import pandas as pd
import numpy as np
import xgboost as xgb

import matplotlib as pyplot
from sklearn.model_selection import train_test_split

train=pd.read_csv("Train_Data.csv")
test=pd.read_csv("Test_Data.csv")

id=test['SEQN']

# print(train.shape)  
train.drop(columns=['SEQN'], inplace=True)
test.drop(columns=['SEQN'], inplace=True)

# print(train.shape)  

# print(train.head(3)

train['age_group']=train['age_group'].map({'Adult':0,'Senior':1})

train=train.dropna(subset=['age_group'])
train['age_group']=train['age_group'].astype(int)
# print(test.columns)

train.fillna(train.mean(numeric_only=True), inplace=True)
test.fillna(test.mean(numeric_only=True), inplace=True)


X=train.drop(columns=['age_group'])
Y=train['age_group']

m=xgb.XGBClassifier(eval_metric='logloss')

m.fit(X,Y)

# print(X.columns[:5])


# print(Y.value_counts())

p = m.predict(test)
s = pd.DataFrame({'age_group':p})


s.to_csv("xgboost_submission.csv",index=False)
