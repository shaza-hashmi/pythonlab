import pandas as pd
from sklearn.preprocessing import MinMax scaler
from sklearn.Neighbors import KNeighbors classifier
 
data { 'sweetness':[2,3,4,5,6],'crunchiness':[9,8,7,6,5] 'label':['apple','apple','orange','carrot','apple']}
df = pd.dataframe (data)
X= df ['sweeetness', 'crunhiness']
X = df['label']
scaler = Normalize scaler()
x_scaled = scaler.fit transform(X)
KNN = KNeighbors classifier
Knn.fit= (X.scaled.Y)
new item =[2,8 ]
new item_scaled = scaler
transform(new item)
prediction = knn predicted(new item_scaled)
printf("the class for carrot sweetness=2,crunchiness=8")
{ prediction[0]}

