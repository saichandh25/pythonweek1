from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pandas as pd
train_df=pd.read_csv("glass.csv")  #Importing the dataset 'glass'
a=train_df.drop('Type',axis=1)  #Preprocessing data
b=train_df['Type']
x_train,x_test,y_train,y_test=model_selection.train_test_split(a, b, test_size=0.2, random_state=0) #splitting data into training data and testing data
model=GaussianNB()    #creating and Training the classifier
model.fit(x_train,y_train)
#Prediction
y_pred=model.predict(x_test)
#Evaluation
print("accuracy score:",metrics.accuracy_score(y_test,y_pred))
print("classification_report\n",metrics.classification_report(y_test,y_pred))
