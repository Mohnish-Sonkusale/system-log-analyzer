import os 
import sys  
import joblib
import pickle

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from preprocessing.preprocess import preprocess_log_line

# Load model and vectorizer
model = joblib.load(os.path.join(project_root, "data", "log_classifier_model.pkl"))
vectorizer = joblib.load(os.path.join(project_root, "data", "tfidf_vectorizer.pkl"))

def predict_log(log_line: str):
    cleaned = preprocess_log_line(log_line)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]
    return pred, prob

if __name__ == "__main__":
    test_log = "CRITICAL ERROR: Kernel panic occurred"
    label, prob = predict_log(test_log)
    print(f"\n🧠 Prediction: {'ERROR' if label else 'NON-ERROR'}")
    print(f"📊 Probabilities: [Non-Issue: {prob[0]:.2f}, Issue: {prob[1]:.2f}]")
