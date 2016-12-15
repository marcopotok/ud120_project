#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
from sklearn import svm
from sklearn.metrics import accuracy_score

# features_train = features_train[:len(features_train)//100]
# labels_train = labels_train[:len(labels_train)//100]

# for x in range(1,5):
c = 10**5

clf = svm.SVC(kernel='rbf', C=c)

t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print("testing time:", round(time()-t0, 3), "s")

print("C =", c , ":",accuracy_score(labels_test, pred))

# print("Element 10: ", clf.predict(features_test[10]))
# print("Element 26: ", clf.predict(features_test[26]))
# print("Element 50: ", clf.predict(features_test[50]))

print("Chris prediction number:", sum(pred), len(pred))

#########################################################
# training time: 141.468 s
# testing time: 14.395 s
# 0.984072810011

