def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import operator
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

income_data = pd.read_csv("income.csv", header=0, delimiter=', ') # comes from https://archive.ics.uci.edu/ml/datasets/census+income

# show all occupation counts of people who made more or less than 50
# print(income_data[(income_data["income"]==">50K")]["occupation"].value_counts())
# print("-----------------------------------")
# print(income_data[(income_data["income"]=="<=50K")]["occupation"].value_counts())

# map gender string values to numbers
income_data["sex"] = income_data["sex"].map({"Male":0, "Female":1})

# map native countries to numbers
income_data["native-country-int"] = income_data["native-country"].apply(lambda country: 1 if country == "United-States" else 0)

# map working class
income_data["workclass-int"] = income_data["workclass"].map({"Private":2, "Self-emp-not-inc":0, "Self-emp-inc":2, "Federal-gov":1, "Local-gov":1, "State-gov":1, "Without-pay":0, "Never-worked":0, "?":1})

# map occupation
income_data["occupation-int"] = income_data["occupation"].apply(lambda occ: 0 if occ in ["Adm-clerical", "Armed-Forces","Priv-house-serv", "Handlers-cleaners"] else 1)

labels = income_data[["income"]] 
data = income_data[["capital-gain", "capital-loss", "education-num", "occupation-int"]]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1)

forest = RandomForestClassifier(n_estimators=150, random_state=2)
forest.fit(train_data, train_labels)

# Show importances of features
print("importances: ", forest.feature_importances_)
print(forest.score(test_data, test_labels)) # 84.45% correct

prediction = {}
for i in range(1, 20):
  tree = DecisionTreeClassifier(random_state=2, max_depth=i)
  tree.fit(train_data, train_labels)
  prediction.update({i: tree.score(test_data, test_labels)})
print("Decision Tree best: ", max(prediction.items(), key=operator.itemgetter(1))) # 84.47% correct

me = np.array([0, 0, 13, 1]).reshape(1, -1)

print("Random Forest Prediction of me: ", forest.predict(me))
