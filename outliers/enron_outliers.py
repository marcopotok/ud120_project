#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset_fixed.pkl", "rb") )
features = ["salary", "bonus"]

# Remove the point rappresentig the total amount of salaries / bonuses
del data_dict["TOTAL"]

data = featureFormat(data_dict, features)


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus )

import operator
salary = 0
outlier_name = ""
for k,v in data_dict.items():
    s = float(v["bonus"])
    if s > salary:
        salary = s
        outlier_name = k

print(outlier_name, salary)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
# matplotlib.pyplot.show()

# bonuses of at least 5 million dollars, and a salary of over 1 million dollars
outlier_names = []
for k,v in data_dict.items():
    if float(v["salary"]) > 10**6 and float(v["bonus"]) >= 5*10**6:
        outlier_names.append(k)

print(outlier_names)