import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv("passengers.csv")
print(passengers.info()) # print range index and types of features
# print(passengers.describe()) 
print(passengers)

# Update sex column to numerical
passengers['Sex'] = passengers['Sex'].map({'female': 1, 'male':0})

# Fill the nan values in the age column
meanAge = np.nanmean(passengers['Age'].values)
passengers['Age'].fillna(value=meanAge, inplace=True)

# Create Age_Class
passengers['Age_Class'] = passengers['Age'] * passengers['Pclass']

# Create a first class column
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)

# Create a second class column
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)

# Create is alone column
passengers['Alone'] = passengers['SibSp'].apply(lambda x: 1 if x < 1 else 0)

# Select the desired features
features = passengers[['Age','Sex', 'FirstClass', 'SecondClass', 'Alone']]
survival = passengers['Survived']

# Perform train, test, split
training_data, test_data, training_labels, test_labels = train_test_split(features, survival, test_size = 0.2, random_state = 10)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
scaler.fit_transform(training_data)
scaler.transform(test_data)

# Create and train the model
model = RandomForestClassifier(n_estimators=2000).fit(training_data, training_labels)

# Score the model on the train data
print("Train data score: ", model.score(training_data, training_labels))

# Score the model on the test data
print("Test data score: ", model.score(test_data, test_labels)) 

# Analyze the coefficients

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0, 1.0])
Rose = np.array([1.0,17.0,1.0,0.0, 0.0])
You = np.array([0.0,26.0,0.0,0.0, 0.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, You])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)

# Make survival predictions!
print("Sample passengers prediciton: ", model.predict(sample_passengers))
