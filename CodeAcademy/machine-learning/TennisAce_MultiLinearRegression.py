import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv("tennis_stats.csv")
print(df.head())

## perform single feature linear regressions here:
X = df[["ServiceGamesPlayed"]]
y = df[["Wins"]]
x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=6)

model = LinearRegression().fit(x_train, y_train)
print(model.score(x_test, y_test))
print(model.score(x_train, y_train))
outcome = model.predict(x_test)

plt.scatter(y_test, outcome, alpha=0.4)
plt.show()

X = df[["DoubleFaults"]]
y = df[["Losses"]]
x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=6)

model = LinearRegression().fit(x_train, y_train)
print(model.score(x_test, y_test))
print(model.score(x_train, y_train))
outcome = model.predict(x_test)

plt.scatter(y_test, outcome, alpha=0.4)
plt.show()

## perform two feature linear regressions here:

X = df[["ServiceGamesPlayed","FirstServePointsWon"]]
y = df[["Wins"]]
x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=6)

model = LinearRegression().fit(x_train, y_train)
print(model.score(x_test, y_test))
print(model.score(x_train, y_train))
outcome = model.predict(x_test)

plt.scatter(y_test, outcome, alpha=0.4)
plt.show()



## perform multiple feature linear regressions here:

features = df.drop(["Winnings", "Year", "Player", "Ranking"], axis=1)
winnings = df[["Winnings"]]
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size = 0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train,winnings_train)

# score model on test data
print('Predicting Winnings with Multiple Features Test Score:', model.score(features_test,winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot predictions against actual winnings
plt.scatter(winnings_test,winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - Multiple Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

