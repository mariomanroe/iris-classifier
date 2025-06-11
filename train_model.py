import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('model/iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved.")
