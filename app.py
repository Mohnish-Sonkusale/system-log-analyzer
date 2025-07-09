import os 
import sys 
import joblib 
import streamlit as st

# Add project root to sys.path to import preprocessing module
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from preprocessing.preprocess import preprocess_log_line

# load the moedl and verctorizer
model_path = os.path.join(project_root, "data", "log_classifier_model.pkl")
vectorizer_path = os.path.join(project_root, "data", "tfidf_vectorizer.pkl")

@st.cache_data
def load_model_and_vectorizer():
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer
model, vectorizer = load_model_and_vectorizer()

def predict_log(log_line : str):
    cleaned = preprocess_log_line(log_line)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]
    return pred, prob

#Stramlit UI 
st.title(" 🖥️ Binary System log Analyser")
st.write("Enter a system log line below to classify it as an Issue or Non-Issue.")

log_input = st.text_area("System Log Line", height=100)

if st.button("Predict"):
    if not log_input.strip():
        st.warning("Please enter a log line to predict.")
    else:
        label, prob = predict_log(log_input)
        st.markdown(f"### Prediction: {'🛑 ISSUE' if label else '✅ NON-ISSUE'}")
        st.markdown(f"**Probabilities:**")
        st.write(f"- Non-Issue: {prob[0]:.2f}")
        st.write(f"- Issue: {prob[1]:.2f}")
