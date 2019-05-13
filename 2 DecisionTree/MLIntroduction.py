# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:39:58 2019

@author: AGKR
"""

# Machine Learning introduction program
# Titanic Machine Learning from Disaster

import pandas as pd    #import pandas package for data frame
from sklearn import tree   #import Tree package from sklearn for decision tree
import os   # import os package

# Read train data file
titanic_train = pd.read_csv("D:\\Data Science\\Kaggle\\Titanic Machine Learning from Disaster\\Data Sources\\train.csv")

# Print data type 
print(type(titanic_train))

# Print number of rows and columns in the data frame
titanic_train.shape

# Print number of columns and its types in the data frame
titanic_train.info()

# Calculate and print basic statatics on the numeric columns on the data frame
titanic_train.describe()

#Let's start the journey with non categorical and non missing data columns
# set imput columns X-axis and out put column y-axis
x_titanic_train = titanic_train[['Pclass','SibSp','Parch']]
y_titanic_train = titanic_train['Survived']

# --- Build the decision tree model ----
dt = tree.DecisionTreeClassifier()

# Build a model based on input data
dt.fit(x_titanic_train,y_titanic_train)

print(type(dt))

# ---- Predict the outcome using decision tree -----
# Read test data file
titanic_test = pd.read_csv("D:\\Data Science\\Kaggle\\Titanic Machine Learning from Disaster\\Data Sources\\test.csv")

# set imput columns X-axsis
x_titanic_test = titanic_test[['Pclass','SibSp','Parch']]

# Predict and write out put on test data based on the model
titanic_test['Survived'] = dt.predict(x_titanic_test)

# Change current working directory
os.chdir("D:\\Data Science\\Kaggle\\Titanic Machine Learning from Disaster\\Data Sources")

# Get current working directory 
#to Check where the submission file is!
os.getcwd()

# Create Submission data file
titanic_test.to_csv("submittion.csv", columns=['PassengerId','Survived'], index=False)
