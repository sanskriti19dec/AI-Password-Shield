# 🛡️ AI-Driven Password Strength Evaluator

A machine learning web application that combines custom character-tokenization matrices with an ensemble learning backend to predict password vulnerability against dictionary and brute-force vectors. Developed independently alongside secondary school studies in Advanced Placement (AP) Cybersecurity and Artificial Intelligence.

## 🚀 Architectural Overview
Rather than relying on primitive regular-expression string matching or static lookups, this architecture implements natural language processing concepts to evaluate human input characteristics:
*   **Vectorization Pipeline:** Leverages `TfidfVectorizer` configured for character-level token analysis (`analyzer='char'`) to convert text credentials into computational matrices.
*   **Classifier Core:** Trains a `RandomForestClassifier` ensemble model against a dataset of verified leaked credentials to map mathematical probabilities of structural safety.
*   **Defensive Guardrails:** Evaluates structural configurations dynamically to provide real-time cryptographic complexity feedback.

## 🛠️ Tech Stack & Ecosystem
*   **Language Backend:** Python 3.11
*   **Data & ML Core:** Pandas, Scikit-Learn
*   **Interface Layer:** Streamlit Web Framework
*   **Deployment Configuration:** Standalone compilation capability via PyInstaller (`.exe`)

## 📊 Performance Analytics
*   **Dataset Dimensions:** Parsed sub-arrays from global compromised credential datasets (Kaggle).
*   **Ensemble Accuracy:** ~94.57% prediction rating across active test/train evaluation sets.
