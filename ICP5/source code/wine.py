import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score    #import required modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv('winequality-red.csv')           #importing data set
print(data.corr()['quality'].sort_values(ascending=False))  #finding the crrelation wrt to quality in descing order
plt.hist(data.quality)
plt.title('Distribution of the Quality')        #histogram
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()
X = data.iloc[:,:11].values         #load required columns for the trainging
Y = data.iloc[:,-1].values
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=0) #spliting for train and test
reg =LinearRegression()  # fitting to linear regression
reg.fit(X_train,Y_train)
y_pred = reg.predict(X_test)
print("mean square value is:",mean_squared_error(Y_test,y_pred)) # mean square error
print("R2 score :",r2_score(Y_test,y_pred))  #R2_score
