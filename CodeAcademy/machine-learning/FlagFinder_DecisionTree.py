import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# data info is located at http://archive.ics.uci.edu/ml/datasets/Flags
flags = pd.read_csv('flags.csv', header=0)
print(flags.columns) # print features
# print(flags.info())
# print(flags.head()) # print first five rows of dataset

labels = flags[["Landmass"]]
data = flags[["Zone", "Area", "Population", "Language",
"Religion", "Bars", "Stripes", "Colors", "Red", "Green", "Blue", "Gold",
"White", "Black", "Orange", "Circles", "Crosses", "Saltires",
"Quarters", "Sunstars", "Crescent", "Triangle", "Icon", "Animate",
"Text"]]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1)

scores = []
for i in range(1, 21):
  for j in range(2, 10):
    tree = DecisionTreeClassifier(random_state=1, max_depth=i, max_leaf_nodes=j)
    tree.fit(train_data, train_labels)
    scores.append(tree.score(test_data, test_label  s))
    print("Depth: {0} Nodes {2} - {1}".format(i, tree.score(test_data, test_labels), j))
print("Best is ", sorted(scores)[-1])
  
# plt.plot(range(1, 21), scores)
# plt.show()

