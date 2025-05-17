
# 🌞 Solar Challenge Week 1

This repository contains code and analysis for the **10 Academy Week 1 Solar Challenge**.  
The challenge focuses on profiling and analyzing solar radiation and environmental data from Benin, Togo, and Sierra Leone to inform solar installation strategies.

---

## 💻 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/kirubhel/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Set up the virtual environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the CI workflow

Push your changes to GitHub or open a pull request to the `main` branch.  
The GitHub Actions workflow (`.github/workflows/ci.yml`) will:
- Install dependencies
- Check Python version

---

## 📁 Project Structure

```
solar-challenge-week1/
├── .vscode/                # Editor configuration
├── .github/workflows/      # GitHub Actions workflows
├── data/                   # (ignored) for storing local CSVs
├── notebooks/              # Jupyter notebooks for EDA
├── scripts/                # Utility and cleaning scripts
├── src/                    # Core logic or modules
├── tests/                  # Unit tests
├── .gitignore              # Files and folders to ignore in git
├── requirements.txt        # Python dependencies
├── README.md               # This file
```

---

## 🔧 CI/CD Pipeline

- A basic GitHub Actions workflow is included to:
  - Automatically install dependencies from `requirements.txt`
  - Run a Python version check for environment validation

---

## ✅ Task 1 Status

✔ Git & GitHub setup  
✔ Virtual environment & dependencies  
✔ CI/CD integration  
✔ Folder structure created  
✔ README documented  

---

## 📌 Next Step

Proceed to **Task 2: Data Profiling and EDA** in the `eda-<country>` branch.
