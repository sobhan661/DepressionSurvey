from pathlib import Path

import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from ml.data.processed.load_data import df

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "depression_classifier.joblib"

X = df.drop(columns="depression_label")
y = df["depression_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2
)

categorical_features = X.select_dtypes(include=["object", "string"]).columns

preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ],
    remainder="passthrough",
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", DecisionTreeClassifier(random_state=42)),
    ]
)

model.fit(X_train, y_train)
score = model.score(X_test, y_test)

print(f"Accuracy: {score:.3f}")

MODEL_PATH.parent.mkdir(exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"Model saved to: {MODEL_PATH}")
