import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


data = pd.read_csv("Cleaned_data.csv")

X = data[["location", "total_sqft", "bath", "bhk"]]
y = data["price"]

ct = ColumnTransformer([
    ("ohe", OneHotEncoder(handle_unknown="ignore"), ["location"])
], remainder="passthrough")

pipe = Pipeline([
    ("transformer", ct),
    ("model", Ridge())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe.fit(X_train, y_train)

print("✅ Model trained successfully!")

# 🟢 Step 5: Model save karo
pickle.dump(pipe, open("model.pkl", "wb"))
