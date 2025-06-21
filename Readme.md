# 🩺 Medical Cost Insurance Prediction Project

Welcome to the **Medical Cost Insurance Prediction Project**! This application predicts medical insurance costs using advanced machine learning models. Built with a React frontend and a Flask backend, it allows users to input personal details (age, BMI, smoker status, etc.) and receive accurate cost predictions. The project showcases a full-stack data science pipeline, from data preprocessing to model deployment, finalized on **June 21, 2025**.

---

## 🚀 Key Features

- Predict insurance costs with a **Hybrid Ensemble model** (XGBoost, CatBoost, LightGBM) achieving **R²: 0.8871**, **RMSE: $4048.21**
- User-friendly **React** interface styled with **Tailwind CSS**
- Robust **Flask API** serving ML predictions
- Comprehensive documentation and Git workflow for collaboration

---

## 📖 Project Overview

The project uses the `insurance.csv` dataset (1,338 records) with features like **age, sex, bmi, children, smoker**, and **region** to predict **charges**.  
The **backend** processes data and runs ML models, while the **frontend** provides an interactive UI.

Ideal for:
- Data science enthusiasts
- Developers
- Academic projects

---

## 🛠️ Tech Stack

- **Frontend**: React, Tailwind CSS, JavaScript (CDN-hosted)
- **Backend**: Python, Flask, Scikit-learn, XGBoost, CatBoost, LightGBM
- **Tools**: Git, Node.js (for frontend dev), Python 3.8+, Conda/Pip, Vercel (for deployment)

---

## 📂 Folder Structure

```
health-cost-insurance/
│
├── frontend/                   # React frontend code
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── styles/
│   ├── package.json
│   └── vercel.json
│
├── backend/                    # Flask backend code
│   ├── api/
│   │   └── app.py
│   ├── models/
│   ├── data/
│   │   └── insurance.csv
│   ├── requirements.txt
│   ├── utils/
│   └── vercel.json
│
├── docs/
│   └── Medical_Cost_Insurance_Prediction_Final_Documentation.md
│
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 📌 Prerequisites

- Git, Node.js v16+, Python 3.8+, Conda (optional)
- Vercel CLI (`npm install -g vercel`)
- GitHub and Vercel accounts

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/health-cost-insurance.git
cd health-cost-insurance
```

---

### 2. Set Up the Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python api/app.py
```

Runs at: http://localhost:5000

---

### 3. Set Up the Frontend

```bash
cd ../frontend
npm install
npm start
```

Runs at: http://localhost:3000

---

### 4. Access the Application

Open your browser at: [http://localhost:3000](http://localhost:3000)

Input your details (age, BMI, etc.) to get a predicted insurance cost.

---

## 👨‍💻 Git Workflow

### ✅ Initialize & Push (if new repo)

```bash
git init
git add .
git commit -m "Initial commit: Project setup"
git remote add origin https://github.com/your-username/health-cost-insurance.git
git branch -M main
git push -u origin main
```

---

### ✅ Typical Workflow

```bash
git pull origin main  # Get latest
# Edit files
git add .
git commit -m "Your message here"
git push origin main
```

---

### ✅ Create Feature Branch

```bash
git checkout -b feature/your-feature
# Make changes
git add .
git commit -m "Add feature"
git push origin feature/your-feature
```

> Open a Pull Request on GitHub to merge.

---

## 🚀 Deployment to Vercel

### 🔹 Backend (Flask)

1. **`backend/requirements.txt`** must include:

```
flask==2.0.1
gunicorn
scikit-learn
xgboost
catboost
lightgbm
pandas
numpy
flask-cors
```

2. **`backend/vercel.json`**:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/api/app.py"
    }
  ]
}
```

3. **Push to GitHub**:

```bash
cd backend
git add .
git commit -m "Configure Flask for Vercel"
git push origin main
```

4. **Deploy on Vercel**:

- Import GitHub repo
- Set **backend/** as root
- Choose "Other" framework
- Deploy & get backend URL

---

### 🔹 Frontend (React)

1. **`frontend/vercel.json`**:

```json
{
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://health-cost-insurance-backend.vercel.app/api/$1"
    }
  ]
}
```

2. **Update API URLs** in `App.jsx` to use `/api/`

3. **Push changes**:

```bash
cd frontend
git add .
git commit -m "Configure React for Vercel"
git push origin main
```

4. **Deploy on Vercel**:

- Import GitHub repo
- Set **frontend/** as root
- Detects React, deploys automatically

---

### 🧪 Post-Deployment

- Open frontend Vercel URL
- Test predictions
- Fix any errors via logs

---

## 📊 Model Performance

| Model           | R²     | RMSE ($) |
|-----------------|--------|----------|
| XGBoost         | 0.8685 | 4517     |
| Hybrid Ensemble | 0.8871 | 4048.21  |

The **Hybrid Ensemble** combines XGBoost, CatBoost, and LightGBM to explain **88.71%** of the variance with low prediction error.

See [`docs/Medical_Cost_Insurance_Prediction_Final_Documentation.md`](docs/Medical_Cost_Insurance_Prediction_Final_Documentation.md) for full analysis.

---

## 🌟 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📝 Documentation

- Data preprocessing
- Model training
- Evaluation metrics
- Visualizations

See: `docs/Medical_Cost_Insurance_Prediction_Final_Documentation.md`

---


---

## 🙌 Acknowledgments

- Dataset: `insurance.csv` (public domain)
- Libraries: Scikit-learn, XGBoost, CatBoost, LightGBM, React, Flask
- Inspired by real-world healthcare cost prediction problems

---

## 📬 Contact

- abdulwahid.shaik147@gmail.com
- haseena7027@gmail.com

> Feel free to open an issue or contribute. Happy coding! 🎉
