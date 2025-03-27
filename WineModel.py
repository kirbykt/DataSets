
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

#Loading data
wine = load_wine()
X = wine.data
y = wine.target

# Convert to DataFrame
df = pd.DataFrame(wine.data, columns=wine.feature_names)

# View the first few rows
print(df.head())

#Print feature names
print(wine.feature_names)

#Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

#Save model
with open('wine_model.pkl', 'wb') as f:
    pickle.dump(model, f)

