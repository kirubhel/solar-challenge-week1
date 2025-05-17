
# ☀️ 10 Academy Week 1 - Solar Challenge

This project is part of the 10 Academy Week 1 challenge focused on exploring solar radiation datasets from **Benin**, **Togo**, and **Sierra Leone**. The goal is to analyze environmental measurements and identify high-potential regions for solar panel deployment using EDA, visualization, and a Streamlit dashboard.

---

## 🧭 Project Overview

- **Challenge Goal:** Support MoonLight Energy Solutions in identifying optimal regions for solar investment.
- **Countries Analyzed:** Benin, Togo, Sierra Leone
- **Methods:** Exploratory Data Analysis, Outlier Detection, Statistical Testing, Dashboarding

---

## 📁 Folder Structure

```
solar-challenge-week1/
├── app/
│   └── main.py                  # Streamlit dashboard
├── data/
│   └── *.csv                    # Cleaned datasets (ignored in Git)
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── compare_countries.ipynb
├── dashboard_screenshots/
│   └── streamlit_ui.png         # Screenshot of dashboard
├── requirements.txt
├── final_report.pdf
└── README.md
```

---

## 🚀 How to Run the Dashboard

1. **Clone the repo**
```bash
git clone https://github.com/kirubhel/solar-challenge-week1.git
cd solar-challenge-week1
```

2. **Create & activate a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```bash
streamlit run app/main.py
```

5. **Open your browser** to:
```
http://localhost:8501
```

---

## 📊 Features

- Country-specific EDA notebooks (Benin, Togo, Sierra Leone)
- Cross-country GHI, DNI, DHI comparison
- One-way ANOVA test for statistical validation
- Interactive dashboard with:
  - Country filter
  - Summary stats table
  - Boxplots of GHI, DNI, DHI

---

## 📄 Final Report

📁 `final_report.pdf`  
Includes:
- Summary of Git setup, EDA, comparison
- Statistical findings
- Dashboard summary
- Strategic recommendations

---

## 📌 Submission Info

- 🔗 GitHub: [https://github.com/kirubhel/solar-challenge-week1](https://github.com/kirubhel/solar-challenge-week1)
- 👤 Submitted by: **Kirubel Gizaw**
- 🗓️ Challenge Duration: May 15–21, 2025
- 🌍 Submitted to: 10 Academy - Week 1 Challenge

---

## ✅ Acknowledgements

- 10 Academy Team: Yabebal, Mahlet, Kerod, Rediet, Rehmet
- Streamlit Docs: https://docs.streamlit.io
- seaborn, matplotlib, pandas

---
