import os
def test_training_artifacts():
    assert os.path.exists("model/artifacts/model.joblib")
    assert os.path.exists("model/artifacts/vectorizer.joblib")
