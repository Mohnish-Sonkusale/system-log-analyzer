# 🖥️ Binary System Log Classifier

This project uses machine learning to classify system log messages as **Issue** or **Non-Issue** — helping IT teams quickly identify critical problems.

---

## 🚀 Quick Start Guide

Follow these steps to set up the environment, train the model (optional), and run the interactive Streamlit app for predictions.

---

## Clone the Repository

```bash
git clone https://github.com/yourusername/log-issue-classifier.git
cd log-issue-classifier
🗂️ Project Structure Overview Binary/

├── app.py # Streamlit app for interactive prediction

├── config/ # Log templates for reference

├── preprocessing/ # Log cleaning functions

├── data/ # Dataset CSV and saved model/vectorizer

├── model/ # (Optional) training scripts or saved models

├── notebooks/ # Jupyter notebooks for training and data generation

├── predict/ # Prediction script (CLI or importable)

├── requirements.txt # Python dependencies

└── README.md # This file


### 1️⃣ Clone the Repository
Open your terminal or PowerShell and run:

git clone https://github.com/yourusername/log-issue-classifier.git

cd log-issue-classifier

---

2️⃣ It’s best practice to use a virtual environment to keep dependencies isolated.
Windows:

--- python -m venv venv

.\venv\Scripts\activate

macOS/Linux:

--- python3 -m venvvenv

source venv/bin/activate

---

3️⃣ Install Required Packages
Install all necessary Python packages by running:

---pip install -r requirements.txt

---

4️⃣ Train the Model (Optional)
If you want to train the model yourself or retrain with new data:

Run the notebook cells step-by-step to:
Load and preprocess data

Train the logistic regression model

Evaluate model performance

Save the trained model and vectorizer

---

5️⃣ Run the Streamlit App for Interactive Prediction
Start the Streamlit app to classify new log lines interactively:

--- streamlit run app.py

A browser window will open. Enter a system log line in the text box. Click Predict to see if it’s an Issue or Non-Issue along with confidence scores.

---

6️⃣ Understanding the Output
Prediction:

🛑 ISSUE means the log indicates a problem. ✅ NON-ISSUE means the log is normal or informational. Probabilities:

Confidence scores for each class (Non-Issue and Issue).
