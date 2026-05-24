# 📧 Email Spam Classifier
 
A machine learning web app that detects whether an email or SMS message is **Spam** or **Not Spam**.
 
🔗 **Live Demo**: [emailspamclassifier-ravi.streamlit.app](https://emailspamclassifier-ravi.streamlit.app)
 
---
 
## How It Works
 
1. User enters an email/SMS message
2. Text is cleaned and preprocessed (lowercasing, tokenization, stopword removal, stemming)
3. Text is converted to numbers using a TF-IDF Vectorizer
4. A trained Random Forest model predicts if it's Spam or Not Spam
5. Result is displayed on screen
---
 
## Tech Stack Used
 
- **Python**
- **Streamlit** — web app interface
- **Scikit-learn** — Random Forest model & TF-IDF Vectorizer
- **NLTK** — text preprocessing
- **Pandas / NumPy** — data handling
---

 
## Run Locally
 
```bash
# 1. Clone the repo
git clone https://github.com/RaviNamdeoo/EmailSpamClassifier.git
cd EmailSpamClassifier
 
# 2. Install dependencies
pip install -r requirements.txt
 
# 3. Run the app
streamlit run app.py
```
 
---
 
## Dataset
 
Used the classic **SMS Spam Collection Dataset** (`spam.csv`) which contains labeled SMS messages as spam or ham (not spam).
 
---
 
## 🤝 Connect
 
Made by **Ravi Namdeo** — feel free to star ⭐ the repo if you found it helpful!
