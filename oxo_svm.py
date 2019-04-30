from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv("Q_table.csv")

X = df[1:10]

y = df[10:11]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle=True)


model = SVR(gamma='scale', C=1.0, epsilon=0.2)

model.fit(X_train, y_train)