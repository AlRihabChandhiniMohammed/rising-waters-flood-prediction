# 🌊 Rising Waters – Flood Prediction System

An AI-powered Flood Prediction System that uses Machine Learning to predict the possibility of floods based on weather and rainfall parameters. The application provides quick predictions through a simple web interface, helping support early warning and disaster preparedness.

---
## 🌐 Live Demo

The Rising Waters application is deployed on Render and can be accessed using the link below:

🔗 **Live Application:**  
[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=render)](https://rising-waters-flood-prediction-y8sg.onrender.com)

> **Note:** This application is hosted on Render's free tier. If the application has been inactive for some time, the first request may take 30–60 seconds while the server wakes up.

## 📌 Project Overview

Floods are among the most destructive natural disasters, causing significant loss of life and property every year. Timely prediction of flood risk enables authorities and communities to take preventive measures before disasters occur.

This project uses historical weather and rainfall data to train multiple machine learning models and predict whether flood conditions are likely to occur. The best-performing model is integrated into a Flask web application, allowing users to enter weather parameters and instantly receive a prediction.

---

## 🎯 Objectives

* Predict flood occurrence using machine learning.
* Improve early flood risk assessment.
* Provide a simple and user-friendly prediction interface.
* Compare multiple machine learning algorithms and select the best-performing model.
* Support future deployment on cloud platforms.

---

## 🚀 Features

* Historical weather data analysis
* Data preprocessing and feature engineering
* Multiple machine learning models

  * Decision Tree
  * Random Forest
  * K-Nearest Neighbors (KNN)
  * XGBoost
* Model evaluation and comparison
* Best model selection and serialization
* Flask-based web application
* Interactive prediction dashboard
* Instant Flood / No Flood prediction

---

## 🛠 Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* XGBoost

### Libraries

* Pandas
* NumPy
* Matplotlib
* Joblib

---

## 📂 Project Structure

```text
rising-waters-flood-prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── dataset/
├── models/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── index.html
│   ├── predict.html
│   └── result.html
└── notebooks / training files
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AlRihabChandhiniMohammed/rising-waters-flood-prediction.git
```

Move into the project directory:

```bash
cd rising-waters-flood-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 💻 How to Use

1. Open the application.
2. Navigate to the prediction page.
3. Enter all required weather parameters.
4. Click **Predict Flood**.
5. View the prediction result.

---

## 📊 Machine Learning Workflow

1. Dataset Collection
2. Data Preprocessing
3. Feature Engineering
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Best Model Selection
8. Model Saving
9. Flask Deployment
10. User Prediction

---

## 📈 Models Used

* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)
* XGBoost

The models were trained and evaluated on historical flood-related weather data. The best-performing model was selected and integrated into the Flask application for prediction.

---

## 🔮 Future Enhancements

* IBM Cloud Deployment
* Real-time Weather API Integration
* User Authentication
* Prediction History
* Interactive Dashboard
* SMS and Email Flood Alerts
* Geographic Flood Risk Mapping

---

## 👥 Team Members

* **Al Rihab Chandhini Mohammed** – Team Lead
* Satyanarayana Akula
* Prem Satya Sai Udatha
* Vijay Kiran Kommoju
* Ranadeep Vinukonda

---

## 📄 License

This project is developed for educational and academic purposes.

---

## ⭐ Acknowledgement

We thank our mentors, faculty members, teammates, and the providers of the flood dataset and open-source libraries that made this project possible.
