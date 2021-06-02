import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv("heart_failure_clinical_records_dataset.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# Taking care of missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(x[:,1:-1])
x[:,1:-1] = imputer.transform(x[:, 1:-1])

# Splitting training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size =0.2, random_state=2)

# Applying Feature Scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:,1:-1]=sc.fit_transform(X_train[:,1:-1])
X_test[:,1:-1]=sc.fit_transform(X_test[:,1:-1])

# Ramdom Forest classification
from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, Y_train)

rf_accuracy = rf_classifier.score(X_test,Y_test)*100
print("Accuracy using Random Forest Classification =>", rf_accuracy,"%")


pickle.dump(rf_classifier, open('rf_model.pkl', 'wb') )