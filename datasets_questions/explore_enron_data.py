#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_fixed.pkl", "rb"))

# number of people
n_people = len(enron_data)
print(n_people)

# number of features
print(len(enron_data["SKILLING JEFFREY K"]))

# number of POIs in the dataset
n_poi = 0
n_no_pay_poi = 0
for k,v in enron_data.items():
    if v["poi"] == 1: 
        n_poi += 1
        if v["total_payments"] == "NaN": n_no_pay_poi += 1
print(n_poi)

# total value of the stock belonging to James Prentice
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

# How many email messages do we have from Wesley Colwell to persons of interest?
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# What’s the value of stock options exercised by Jeffrey K Skilling?
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# print(enron_data["SKILLING JEFFREY K"])

# How many folks in this dataset have a quantified salary?
# What about a known email address?
n_salary = 0
n_email = 0
n_no_payments = 0
for k,v in enron_data.items():
    if not v["salary"] == "NaN": n_salary += 1
    if not v["email_address"] == "NaN": n_email += 1
    if v["total_payments"] == "NaN": n_no_payments += 1
print(n_salary, n_email)

# How many people in the E+F dataset (as it currently exists) have “NaN”
# for their total payments? What percentage of people in the dataset 
# as a whole is this?
print(n_no_payments, round(n_no_payments / n_people,3))

# How many POIs in the E+F dataset have “NaN” for their total payments? 
# What percentage of POI’s as a whole is this?
print(n_no_pay_poi, round(n_no_pay_poi / n_poi, 3))

# For now, the takeaway message is to be very careful about
# introducing features that come from different sources
# depending on the class! It’s a classic way to accidentally
# introduce biases and mistakes.