# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:09:15 2019

@author: AGKR
"""

# Print decision tree

# import packages
import os
import io
import pandas as pd
from sklearn import tree
import pydot

# read train data file
titanic_train = pd.read_csv("D:/Data Science/Kaggle/Titanic Machine Learning from Disaster/Data Sources/train.csv")

#set input columns and out put column
x_train = titanic_train[['Pclass','SibSp','Parch']]
y_train = titanic_train['Survived']

# create decision tree
dt = tree.DecisionTreeClassifier()

# Build the decision tree Model
dt.fit(x_train,y_train)

#visualize the decission tree
objStringIO = io.StringIO()

tree.export_graphviz(dt, out_file = objStringIO, feature_names=x_train.columns)

#Use out_file = objStringIO to getvalues()
file1 = pydot.graph_from_dot_data(objStringIO.getvalue())

print(type(file1[0]))
# Change current working directory
os.chdir("D:/Data Science/Kaggle/Titanic Machine Learning from Disaster/Data Sources")

# create decision tree pdf
file1[0].write_pdf("DecisionTree 0513.pdf")
