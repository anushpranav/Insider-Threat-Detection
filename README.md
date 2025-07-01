# Insider Threat Detection using Machine Learning

Detecting insider threats is a critical aspect of organizational security. This project leverages advanced machine learning techniques to analyze email communication patterns and content, identifying potential insider threats within an organization.

---

## 🚀 Project Overview

**Objective:**
> Automatically detect suspicious insider activities by analyzing email metadata and content using a combination of supervised and unsupervised machine learning models.

**Key Outcomes:**
- Identify high-risk emails and users.
- Generate risk scores for users based on their email behavior.
- Provide explainable outputs for security analysts.

---

## ✨ Features

- **Comprehensive Email Analysis:** Utilizes both metadata and content from emails.
- **Hybrid ML Approach:** Combines anomaly detection (unsupervised) and classification (supervised) models.
- **Explainable Results:** Outputs include explanations for flagged emails and user risk scores.
- **Scalable Pipeline:** Designed to handle large organizational datasets.

---

## 📊 Dataset

- **Source:** CERT Email Dataset
- **Attributes:**
  - id, date, user, pc, to, cc, bcc, from, size, attachments, content
- **Preprocessing:**
  - Time feature extraction (hour, day of week, weekend/working hours)
  - Recipient analysis (internal/external, domain matching)
  - Text processing (tokenization, lemmatization, TF-IDF)

---

## 🧠 Approach

1. **Data Preprocessing:**
   - Clean and enrich email records with behavioral and content-based features.
2. **Feature Engineering:**
   - Extract features such as recipient counts, external domain ratios, time-based flags, and content statistics.
3. **Anomaly Detection:**
   - Use Isolation Forest and One-Class SVM to flag unusual emails.
4. **Supervised Classification:**
   - Train a Random Forest classifier to distinguish between normal and suspicious emails (if labeled data is available).
5. **Risk Scoring:**
   - Aggregate email-level anomalies to compute user risk scores.
6. **Output Generation:**
   - Export high-risk emails and user risk scores for further analysis.

---

## ⚙️ Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Insider-Threat-Detection-DPSA
   ```
2. **Install dependencies:**
   - Recommended: Use a virtual environment (e.g., `venv`, `conda`).
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - If `requirements.txt` is missing, install:
     ```bash
     pip install pandas numpy scikit-learn matplotlib seaborn nltk imbalanced-learn
     ```
3. **Download the dataset:**
   - Place the CERT email dataset in the `dataset/` directory as `cert_email_dataset.csv`.

---

## 📝 Usage

- **Jupyter Notebook:**
  - Open `insider_threat_detection.ipynb` to explore the full workflow: data loading, preprocessing, feature engineering, modeling, and output generation.
- **Data Reduction Script:**
  - Use `dataset_reducer.py` to extract a subset of the dataset for quick experimentation.
    ```bash
    python dataset_reducer.py
    ```
- **Outputs:**
  - `generated_data/high_risk_emails.csv`: List of emails flagged as high risk, with explanations.
  - `generated_data/user_risk_scores.csv`: Risk scores for each user.
  - `models/insider_threat_model.pkl`: Trained model (if applicable).

---

## 📈 Outputs

- **High-Risk Emails:**
  - CSV file with detailed features, anomaly scores, ML predictions, and explanations for each flagged email.
- **User Risk Scores:**
  - CSV file summarizing risk metrics for each user (mean, max, count, suspicious percentage).

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
