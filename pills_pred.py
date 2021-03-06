# -*- coding: utf-8 -*-
"""pills_pred.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ANWJxMStVoFjXT74B_xKu0NfuqXp7A98
"""

import zipfile
from google.colab import drive

drive.mount('/content/drive/')

zip_ref = zipfile.ZipFile('/pills.zip', 'r')
zip_ref.extractall()
zip_ref.close()

import pandas as pd



import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import resample

df = pd.read_csv('/content/drug200.csv')

df



df.dropna(inplace = True)

from sklearn.preprocessing import LabelEncoder

le =  LabelEncoder()
for i in df:
    if df[i].dtype=='object':
        df[i] = le.fit_transform(df[i])
    else:
        continue

df

X = df[['Age',	'Sex', 'Na_to_K',	'BP',	'Drug']].values
y = df['Cholesterol'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import f1_score

model = RandomForestClassifier()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(y_pred[:15])



from sklearn.metrics import  recall_score, accuracy_score, classification_report





accuracy = accuracy_score(y_pred, y_test)





print(accuracy)

print(classification_report(y_test,y_pred))
print('F1 Score: ',f1_score(y_test,y_pred,pos_label=1))

from sklearn.metrics import confusion_matrix
confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)

print(confmat)

fig, ax =plt.subplots(figsize=(12.5, 12.5))
ax.matshow(confmat,  cmap=plt.cm.Blues, alpha=0.30)
for i in range(confmat.shape[0]):
  for j in range(confmat.shape[1]):
    ax.text(x=j, y=i,
            s=confmat[i, j],
            va='center', ha='center')
    plt.title('Using the Random Forest model at 76% accuracy prediction in the drug dataset for identifying false negatives and false positives as well as true positives and true negatives in this confusion matrix. With 0 for high Cholesetorol and 1 for normal Cholesterol.')
    plt.xlabel('Predicted label')
    plt.ylabel('True Label')
