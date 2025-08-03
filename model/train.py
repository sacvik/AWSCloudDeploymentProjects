import pandas as pd
import joblib
import yaml
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

with open("model/config.yaml") as f:
    config = yaml.safe_load(f)

os.makedirs(config["artifacts_dir"], exist_ok=True)
data = pd.read_csv(config["train_data_path"])
X = data[config["feature_column"]]
y = data[config["target_column"]]

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=config["val_split"], random_state=config["random_seed"]
)
vectorizer = TfidfVectorizer(max_features=config["max_features"])
X_train_vec = vectorizer.fit_transform(X_train)
model = LogisticRegression(
    multi_class="multinomial",
    solver="lbfgs",
    max_iter=config["max_iter"],
    random_state=config["random_seed"]
)
model.fit(X_train_vec, y_train)

joblib.dump(model, os.path.join(config["artifacts_dir"], "model.joblib"))
joblib.dump(vectorizer, os.path.join(config["artifacts_dir"], "vectorizer.joblib"))
