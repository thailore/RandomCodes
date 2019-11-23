import codecademylib3_seaborn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load Data
breast_cancer_data = load_breast_cancer()

# Split Data into labels and features and testing vs training
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

accuracies = []
k_list = range(1, 101)

for i in range(1, 101):
  # Create model
  classifier = KNeighborsClassifier(n_neighbors=i)
  # Train model
  classifier.fit(training_data, training_labels)
  # Test accuracy of model
  score = classifier.score(validation_data, validation_labels)
  accuracies.append(score)
  print("With {} neighbors accuracy is: {}", i, score)

plt.xlabel("K - Neighbors")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.plot(k_list, accuracies)
plt.show()
