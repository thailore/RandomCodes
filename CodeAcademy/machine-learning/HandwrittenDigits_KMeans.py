import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

## Hand written digits classifier
## given an 8x8 image with certain pixels, determine what digit it is

digits = datasets.load_digits()
# print(digits.DESCR)
# Figure size (width, height)

# fig = plt.figure(figsize=(6, 6))

# # Adjust the subplots 

# fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# # For each of the 64 images

# for i in range(64):

#     # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position

#     ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

#     # Display an image at the i-th position

#     ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

#     # Label the image with the target value

#     ax.text(0, 7, str(digits.target[i]))

# plt.show()

model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)

fig = plt.figure(figsize=(8,3))
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

for i in range(10):
  ax = fig.add_subplot(2,5,1 + i)
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()  


## 6 0 3 2
new_samples = np.array([
[0.00,0.00,0.00,3.66,3.20,0.00,0.00,0.00,0.00,0.00,4.20,7.62,4.96,0.00,0.00,0.00,0.00,0.84,7.55,4.65,0.00,0.00,0.00,0.00,0.00,3.21,7.62,4.65,5.34,5.34,5.19,1.98,0.00,4.27,7.62,7.63,5.95,5.34,7.02,5.88,0.00,5.19,7.62,3.20,0.00,0.61,6.40,5.88,0.00,6.94,7.02,2.36,4.43,7.17,7.40,2.52,0.00,4.43,7.63,7.62,7.40,5.04,1.22,0.00],
[0.00,0.00,0.00,3.58,5.34,5.34,5.11,2.29,0.00,0.00,2.36,7.62,6.94,5.34,6.71,7.32,0.00,0.00,5.11,7.01,0.38,0.00,1.83,7.62,0.00,0.00,7.25,4.50,0.00,0.00,1.52,7.62,0.00,0.76,7.62,3.28,0.00,0.00,2.06,7.62,0.00,0.76,7.62,3.05,0.00,0.23,5.95,7.17,0.00,0.23,7.32,6.02,3.89,5.72,7.55,2.36,0.00,0.00,3.13,6.48,6.86,6.71,2.67,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.99,7.40,7.62,7.40,2.52,0.00,0.00,0.00,0.08,2.82,3.43,7.17,5.80,1.52,0.99,0.00,2.52,5.72,7.47,7.62,7.62,7.62,7.40,0.84,7.09,7.02,4.58,2.98,2.06,4.04,7.62,1.30,0.46,0.08,0.00,0.00,1.68,7.02,6.03,0.00,0.00,0.76,4.58,6.41,7.63,6.71,1.07,0.00,0.00,1.98,6.79,5.42,3.13,0.46,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.07,4.96,6.63,6.86,6.41,0.54,0.00,0.00,4.12,7.24,4.65,4.96,7.62,1.53,0.00,0.00,0.15,0.46,0.00,4.19,7.55,0.69,0.00,0.00,0.00,0.00,2.29,7.55,4.73,0.00,0.00,0.00,0.00,1.76,7.17,6.79,2.75,3.89,4.12,0.00,2.36,7.17,7.62,7.62,7.62,7.24,6.03,0.15,6.10,7.24,5.19,3.28,1.22,0.15,0.00,0.00]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
## predicted 6692
print(model.score(digits.data, digits.target))
