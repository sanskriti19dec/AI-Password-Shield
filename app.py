import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Configure the Web Page Layout
st.set_page_config(page_title="AI Password Shield", page_icon="🛡️", layout="centered")

st.title("🛡️ AI-Driven Password Strength Evaluator")
st.markdown("Fusing Machine Learning with Cybersecurity Principles to detect vulnerable credentials.")
st.write("---")

# Cache the data loading and training so it runs incredibly fast after the first load
@st.cache_resource
def train_ai_model():
    # 1. Load the dataset (using head(50000) for high speed on laptops)
    data = pd.read_csv("data.csv", on_bad_lines='skip')
    data = data.dropna()
    data = data.head(50000) 
    
    # 2. Tokenizer function
    def make_tokens(txt):
        return [char for char in txt]
    
    # 3. Vectorize characters
    vectorizer = TfidfVectorizer(tokenizer=make_tokens, analyzer='char')
    X = vectorizer.fit_transform(data['password'])
    y = data['strength']
    
    # 4. Train Model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    return vectorizer, model

# Status bar while training the backend engine
with st.spinner("Initializing AI Core Engine... Please wait..."):
    vectorizer, model = train_ai_model()
st.success("AI Core Engine Trained Successfully!")

st.write("### Test Your Password Vulnerability")
user_password = st.text_input("Enter a password to evaluate:", type="password", help="Type your password here to let the AI analyze its structure.")

if user_password:
    # Cybersecurity Metric Calculations
    has_upper = any(c.isupper() for c in user_password)
    has_digit = any(c.isdigit() for c in user_password)
    has_special = any(not c.isalnum() for c in user_password)
    
    # Run the machine learning evaluation array
    transformed_input = vectorizer.transform([user_password])
    prediction = model.predict(transformed_input)[0]
    
    # Display Visual Metric Ratings
    st.write("#### Evaluation Dashboard")
    if prediction == 0:
        st.error("🚨 AI Prediction Rating: WEAK PASSWORD")
        st.progress(25)
    elif prediction == 1:
        st.warning("⚠️ AI Prediction Rating: MEDIUM PASSWORD")
        st.progress(60)
    else:
        st.success("✅ AI Prediction Rating: STRONG PASSWORD")
        st.progress(100)
        
    # Build Cybersecurity Architectural Feedback Cards
    st.write("---")
    st.write("#### Defensive Architecture Feedback:")
    
    if len(user_password) < 12:
        st.info("💡 **Length Notice:** Your password is short. Security policies require 12+ characters to disrupt brute-force attacks.")
    
    if not (has_upper and has_digit and has_special):
        st.info("💡 **Complexity Notice:** Incorporate uppercase characters, numeric configurations, and distinct special characters (`@, #, $, &`) to eliminate dictionary attack risks.")
        
    if len(user_password) >= 12 and has_upper and has_digit and has_special:
        st.balloons()
        st.success("🌟 Architectural Profile: Exceptional entropy level. Excellent defense configurations detected!")
