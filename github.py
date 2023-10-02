# -*- coding: utf-8 -*-
"""Github

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L2t5oOWOtnazR5MOloPlApApLZrE3xd3
"""

import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv(r"/content/drive/MyDrive/Final Project/Final Project/Dataset/heart.csv")

df.shape

# drop any row that contains a NaN value
df.dropna(inplace=True)

df.shape

column_values = df["cp"].unique()
print(column_values)

sns.barplot(x = 'cp', y = 'target', data = df)

sns.barplot(x = 'sex', y = 'target', data = df)

from sklearn.model_selection import train_test_split
newdata=df.dropna(axis=0,how='any')
print(newdata.shape)
X = df.drop('target', axis=1)
Y = df['target']
Y1=list(Y)

Y=pd.DataFrame(Y)
print(X.shape)
print(Y.shape)
print(Y)
type(X)
type(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify = Y, random_state=1)
print(X_train.shape,X_test.shape,Y_train.shape,Y_test.shape)
print(X_train.mean(), X_test.mean(), X.mean())

initial_number_of_data_points = len(X)


def get_unique(X_matrix, y_vector):
    Xy = list(set(list(zip([tuple(x) for x in X_matrix], y_vector))))
    X_matrix = [list(l[0]) for l in Xy]
    y_vector = [l[1] for l in Xy]
    return X_matrix, y_vector


X, Y = get_unique(X, Y)
data_points_removed = initial_number_of_data_points - len(X)
print("Number of duplicates removed:", data_points_removed )

# Random Forest Classifier
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.model_selection import KFold, train_test_split

newdata = df.dropna(axis=0, how='any')
X = newdata.drop('target', axis=1)
Y = newdata['target']

# Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify=Y, random_state=1)

# Initialize a Random Forest classifier
rfclassifier = RandomForestClassifier()   #

# Fit the Random Forest classifier to your training data
rfclassifier.fit(X_train, np.ravel(Y_train))

# Make predictions on your test data
y_pred = rfclassifier.predict(X_test)

# Calculate various performance metrics
accuracy = accuracy_score(y_pred, Y_test)
precision=precision_score(y_pred,Y_test)
recall = recall_score(y_pred, Y_test)
f1 = 2 * (precision * recall) / (precision + recall)
cm = confusion_matrix(Y_test, y_pred)
sensitivity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
specificity = cm[1, 0] / (cm[1, 0] + cm[1, 1])

# Print the performance metrics
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Precision: {:.2f}%".format(precision * 100))
print("Recall: {:.2f}%".format(recall * 100))
print("F1 Score: {:.2f}".format(f1))
print("Sensitivity: {:.2f}".format(sensitivity))
print("Specificity: {:.2f}".format(specificity))

# Initialize Bagging and Boosting classifiers using Logistic Regression as the base estimator
baggclassifier = BaggingClassifier(base_estimator=rfclassifier, n_estimators=300)
boostclassifier = AdaBoostClassifier(base_estimator=rfclassifier, algorithm="SAMME", n_estimators=300)

# Define a function to run k-fold cross-validation with a classifier
def run_kfold(clf):
    kf = KFold(n_splits=10, shuffle=False)
    outcomesaccuracy = []
    outcomesprecision = []
    outcomesrecall = []
    outcomesf1 = []
    fold = 0

    for train_index, test_index in kf.split(X):
        fold += 1
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = Y.iloc[train_index], Y.iloc[test_index]
        clf.fit(X_train, np.ravel(y_train))
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = 2 * (precision * recall) / (precision + recall)

        outcomesaccuracy.append(accuracy)
        outcomesprecision.append(precision)
        outcomesrecall.append(recall)
        outcomesf1.append(f1)

        print("Fold {0} accuracy: {1}".format(fold, accuracy))
        print("Fold {0} precision: {1}".format(fold, precision))
        print("Fold {0} recall: {1}".format(fold, recall))
        print("Fold {0} f1: {1}".format(fold, f1))

    mean_accuracy_outcome = np.mean(outcomesaccuracy)
    mean_precision_outcome = np.mean(outcomesprecision)
    mean_recall_outcome = np.mean(outcomesrecall)
    mean_f1_outcome = np.mean(outcomesf1)

    print("Mean Accuracy: {:.2f}".format(mean_accuracy_outcome * 100))
    print("Mean Precision: {:.2f}".format(mean_precision_outcome * 100))
    print("Mean Recall: {:.2f}".format(mean_recall_outcome * 100))
    print("Mean F1: {:.2f}".format(mean_f1_outcome))

# Run k-fold cross-validation with the boosting classifier
print("Running k-fold cross-validation with Boosting Classifier:")
run_kfold(boostclassifier)

#Logistic Regression Classifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings("ignore")
lcclassifier = LogisticRegression()
lcclassifier.fit(X_train, np.ravel(Y_train))
y_pred = lcclassifier.predict(X_test)
accuracy=accuracy_score(y_pred,Y_test)
precision=precision_score(y_pred,Y_test)
recall=recall_score(y_pred,Y_test)
f1=2*(precision*recall)/(precision+recall)
cm=confusion_matrix(Y_test,y_pred)
sensitivity=cm[0,0]/(cm[0,0]+cm[0,1])
specificity=cm[1,0]/(cm[1,0]+cm[1,1])
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("Precision: {:.2f}%".format(precision * 100))
print("Recall: {:.2f}%".format(recall * 100))
print("F1 Score: {:.2f}".format(f1))
print("Sensitivity: {:.2f}".format(sensitivity))
print("Specificity: {:.2f}".format(specificity))

print("Bagging Classifier")
baggclassifier=BaggingClassifier(base_estimator=lcclassifier,n_estimators=300)
print("Boosting Classifier")
boostclassifier=AdaBoostClassifier(base_estimator=lcclassifier,algorithm="SAMME",n_estimators=300)
def run_kfold(clf):
    kf = KFold(10,shuffle=False)
    outcomesaccuracy = []
    outcomesprecision = []
    outcomesrecall = []
    outcomesf1 = []
    fold = 0
    for train_index, test_index in kf.split(X):
        fold += 1
        X_train, X_test = X.values[train_index], X.values[test_index]
        y_train, y_test = Y.values[train_index], Y.values[test_index]
        clf.fit(X_train, np.ravel(y_train))
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        precision=precision_score(y_test,predictions)
        recall=recall_score(y_test,predictions)
        f1=2*(precision*recall)/(precision+recall)
        cm=confusion_matrix(Y_test,y_pred)
        sensitivity=cm[0,0]/(cm[0,0]+cm[0,1])
        specificity=cm[1,0]/(cm[1,0]+cm[1,1])
        outcomesaccuracy.append(accuracy)
        outcomesprecision.append(precision)
        outcomesrecall.append(recall)
        outcomesf1.append(f1)
        print("Fold {0} accuracy: {1}".format(fold, accuracy))
        print("Fold {0} precision: {1}".format(fold, precision))
        print("Fold {0} recall: {1}".format(fold, recall))
        print("Fold {0} f1: {1}".format(fold, f1))
        mean_accuracy_outcome = np.mean(outcomesaccuracy)
        mean_precision_outcome = np.mean(outcomesprecision)
        mean_recall_outcome = np.mean(outcomesrecall)
        mean_f1_outcome = np.mean(outcomesf1)
        print("Mean Accuracy: {0}".format(mean_accuracy_outcome))
        print("Mean Precision: {0}".format(mean_precision_outcome))
        print("Mean Recall: {0}".format(mean_recall_outcome))
        print("Mean F1: {0}".format(mean_f1_outcome))

run_kfold(boostclassifier)

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
dtclassifier = DecisionTreeClassifier()
dtclassifier.fit(X_train, np.ravel(Y_train))
y_pred = dtclassifier.predict(X_test)
accuracy=accuracy_score(y_pred,Y_test)
precision=precision_score(y_pred,Y_test)
recall=recall_score(y_pred,Y_test)
f1=2*(precision*recall)/(precision+recall)
cm=confusion_matrix(Y_test,y_pred)
sensitivity=cm[0,0]/(cm[0,0]+cm[0,1])
specificity=cm[1,0]/(cm[1,0]+cm[1,1])
print(accuracy*100)
print(precision*100)
print(recall*100)
print(f1)
print(sensitivity)
print(specificity)
print("Bagging Classifier")
baggclassifier=BaggingClassifier(base_estimator=dtclassifier,n_estimators=300)
print("Boosting Classifier")
boostclassifier=AdaBoostClassifier(base_estimator=dtclassifier,algorithm="SAMME",n_estimators=150)
def run_kfold(clf):
    kf = KFold(10,shuffle=False)
    outcomesaccuracy = []
    outcomesprecision = []
    outcomesrecall = []
    outcomesf1 = []
    fold = 0
    for train_index, test_index in kf.split(X):
        fold += 1
        X_train, X_test = X.values[train_index], X.values[test_index]
        y_train, y_test = Y.values[train_index], Y.values[test_index]
        clf.fit(X_train, np.ravel(y_train))
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        precision=precision_score(y_test,predictions)
        recall=recall_score(y_test,predictions)
        f1=2*(precision*recall)/(precision+recall)
        cm=confusion_matrix(Y_test,y_pred)
        sensitivity=cm[0,0]/(cm[0,0]+cm[0,1])
        specificity=cm[1,0]/(cm[1,0]+cm[1,1])
        outcomesaccuracy.append(accuracy)
        outcomesprecision.append(precision)
        outcomesrecall.append(recall)
        outcomesf1.append(f1)
        print("Fold {0} accuracy: {1}".format(fold, accuracy))
        print("Fold {0} precision: {1}".format(fold, precision))
        print("Fold {0} recall: {1}".format(fold, recall))
        print("Fold {0} f1: {1}".format(fold, f1))
        mean_accuracy_outcome = np.mean(outcomesaccuracy)
        mean_precision_outcome = np.mean(outcomesprecision)
        mean_recall_outcome = np.mean(outcomesrecall)
        mean_f1_outcome = np.mean(outcomesf1)
        print("Mean Accuracy: {0}".format(mean_accuracy_outcome))
        print("Mean Precision: {0}".format(mean_precision_outcome))
        print("Mean Recall: {0}".format(mean_recall_outcome))
        print("Mean F1: {0}".format(mean_f1_outcome))

run_kfold(boostclassifier)

