#neural network
#first try

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

df= pd.read_excel("Labels.xlsx")
df2=pd.get_dummies(df)



#print(df2.head())

X_df2 = df2.iloc[:,2:] #bien
y_df2 = df2.iloc[:,1] # bien

X_train, X_test, y_train, y_test = train_test_split(X_df2, y_df2, random_state=0)# split intro train and test


mlp = MLPClassifier(hidden_layer_sizes=(200,100,100, 50, 25), max_iter=10000)

mlp.fit(X_train, y_train.values.ravel())

from sklearn.metrics import classification_report, confusion_matrix
predictions = mlp.predict(X_test)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))


#Exportar
import pickle
with open("NN1mlp.txt","wb") as fp:
    pickle.dump(mlp, fp)



    
#importar
##with open("NN1mlp.txt", "rb") as fp:   # Unpickling    
##    mlp = pickle.load(fp)
