import numpy as np
from sklearn.dataset import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.matrics import accuracy_score

iris=load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_test,y_train=train_test_split(x,y,test_size=0.2,random_state=42)
model = GaussianNB
model.fit(x_train,y_train)

y_pred= model.predict(x_test)
print("predicted:",y_pred)
print("accuracy",accuracy_score(y_test,y_pred))
