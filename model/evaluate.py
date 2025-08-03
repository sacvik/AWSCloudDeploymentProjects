import pandas as pd
import joblib
import yaml
from sklearn.metrics import classification_report

with open("model/config.yaml") as f:
    config = yaml.safe_load(f)

data = pd.read_csv(config["test_data_path"])
X_test = data[config["feature_column"]]
y_test = data[config["target_column"]]

model = joblib.load(f"{config['artifacts_dir']}/model.joblib")
vectorizer = joblib.load(f"{config['artifacts_dir']}/vectorizer.joblib")

X_test_vec = vectorizer.transform(X_test)
y_pred = model.predict(X_test_vec)
report = classification_report(y_test, y_pred)
print(report)
