import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load dataset
df = pd.read_csv('disease_data.csv')

print("📦 Columns:", df.columns.tolist())
print("📊 Unique diseases:", df['disease'].unique())

# Features (symptoms)
X = df[['fever', 'cough', 'fatigue', 'headache']]

# Target (disease)
y = df['disease']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Accuracy check
acc = model.score(X_test, y_test)
print(f"✅ Model trained with accuracy: {acc:.2f}")

# Save model
joblib.dump(model, 'disease_model.pkl')
print("💾 Model saved as disease_model.pkl")
