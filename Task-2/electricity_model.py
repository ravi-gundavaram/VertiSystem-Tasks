import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the dataset
data = pd.read_csv("data/clean_data.csv")

print(data.info())
print(data.describe())

# Encode categorical features
label_encoder = LabelEncoder()
data['sectorName'] = label_encoder.fit_transform(data['sectorName'])
data['stateDescription'] = label_encoder.fit_transform(data['stateDescription'])

# Drop unnecessary columns
data = data.drop(['customers', 'revenue', 'sales'], axis=1)

# Features and target
X = data.drop(['price'], axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning using GridSearchCV
param_grid = {'n_estimators': [50, 100, 150, 200]}
rf = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, scoring='neg_mean_squared_error', cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Train the best model
best_rf = grid_search.best_estimator_
best_rf.fit(X_train, y_train)

# Predictions and evaluation
y_pred = best_rf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(best_rf, f)

