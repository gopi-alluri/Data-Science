# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:29:18 2019

@author: AGKR
"""

import pandas as pd
from sklearn import tree
import io
import pydot #if we need to use any external .exe files....
import os

#os.chdir("D:/Data Science/Data/")
#os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
pd.set_option("display.max_column",30)
titanic_train = pd.read_csv("D:/Data Science/Kaggle/Titanic Machine Learning from Disaster/Data Sources/train.csv")

#Transformation of non numneric cloumns to 1-Hot Encoded columns
#There is an exception with the Pclass. Though it's co-incidentally a number column but it's a Categoric column(Even common-sence wise).

#Transform categoric to One hot encoding using get_dummies
titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
#titanic_train1.head(10)
#titanic_train1.info()

# set imput columns X-axis and out put column y-axis
x_titanic_train = titanic_train1.drop(['PassengerId','Survived','Name','Age','Ticket','Fare','Cabin'], axis=1)
y_titanic_train = titanic_train1['Survived']

# --- Build the decision tree model ----
dt = tree.DecisionTreeClassifier()

# Build a model based on input data
dt.fit(x_titanic_train,y_titanic_train)

print(type(dt))

# ---- Predict the outcome using decision tree -----
# Read test data file
titanic_test = pd.read_csv("D:\\Data Science\\Kaggle\\Titanic Machine Learning from Disaster\\Data Sources\\test.csv")

#Transform categoric to One hot encoding using get_dummies
titanic_test1 = pd.get_dummies(titanic_test, columns=['Pclass', 'Sex', 'Embarked'])

# set imput columns X-axis
x_titanic_test = titanic_test1.drop(['PassengerId','Name','Age','Ticket','Fare','Cabin'], axis=1)

# Predict and write out put on test data based on the model
titanic_test['Survived'] = dt.predict(x_titanic_test)
titanic_test.info('Survived')

# Change current working directory
os.chdir("D:\\Data Science\\Kaggle\\Titanic Machine Learning from Disaster\\Data Sources")

# Get current working directory 
#to Check where the submission file is!
os.getcwd()

# Create Submission data file
titanic_test.to_csv("submittion with oneHotEncoding.csv", columns=['PassengerId','Survived'], index=False)
