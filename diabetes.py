import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle

df=pd.read_csv('diabetes.csv')

X=df.iloc[:,0:8]
Y=df['Outcome']


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, stratify=Y,random_state=1)

classifier = svm.SVC(kernel='linear')

# training 
classifier.fit(X_train, Y_train)

pickle.dump(classifier, open('diabetes.pkl', 'wb'))
  
