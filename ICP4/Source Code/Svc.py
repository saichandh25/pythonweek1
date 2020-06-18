import pandas as pd
from sklearn import metrics
from sklearn import model_selection
from sklearn.svm import SVC
train_df = pd.read_csv('./glass.csv')   # Importing the dataset 'glass'
a = train_df.drop('Type', axis=1)     # Preprocessing data
b = train_df['Type']
x_train, x_test, y_train, y_test = model_selection.train_test_split(a, b, test_size=0.3, random_state=0)   # splitting data into training data and testing data
model = SVC(kernel="linear")    # creating and Training the classifier
model.fit(x_train, y_train)
y_pred = model.predict(x_test)    # Prediction
print("accuracy score:", metrics.accuracy_score(y_test, y_pred))   # Evaluation
print("classification_report\n", metrics.classification_report(y_test, y_pred))
