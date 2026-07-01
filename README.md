# Rising-Waters-Flood-Prediction

A machine learning-based flood prediction system that analyzes historical weather and rainfall data to forecast flood risks, enabling early warnings and informed decision-making for disaster management.

---

## Problem Statement

Flooding causes significant damage to life, property, and infrastructure worldwide. Traditional flood forecasting methods often lack accuracy and timeliness. This project leverages machine learning to predict flood occurrences using historical meteorological data, providing actionable insights to authorities and communities.

---

## Objectives

- Collect and preprocess historical weather and rainfall datasets.
- Perform exploratory data analysis (EDA) to identify key flood-inducing factors.
- Train and compare multiple ML models (Decision Tree, Random Forest, KNN, XGBoost).
- Select the best-performing model and deploy it via a Flask web application.
- Provide an intuitive interface for real-time flood risk prediction.

---

## Project Workflow

The project follows a structured machine learning development lifecycle consisting of five major phases:

### Epic 1: Data Collection
- Download the flood prediction dataset.
- Load the dataset into a Jupyter Notebook for analysis.

### Epic 2: Visualizing and Analysing the Data
- Import the required Python libraries.
- Explore the dataset.
- Perform univariate analysis.
- Perform multivariate analysis.
- Generate descriptive statistics and visualizations.

### Epic 3: Data Pre-processing
- Handle missing values.
- Detect and treat outliers.
- Encode categorical variables.
- Split the dataset into training and testing sets.
- Apply feature scaling.

### Epic 4: Model Building
- Train Decision Tree, Random Forest, KNN, and XGBoost models.
- Compare model performance using evaluation metrics.
- Select the best-performing model.
- Save the trained model as a .pkl file.

### Epic 5: Application Building
- Develop the HTML user interface.
- Build the Flask application.
- Integrate the trained model.
- Test and validate the application.

---

## Features

- Data preprocessing and feature engineering pipeline.
- Multiple ML model training with hyperparameter tuning.
- Model comparison and evaluation using accuracy, precision, recall, F1-score.
- Flask-based web interface for predictions.
- Visualizations of model performance and feature importance.

---

## Technology Stack

| Category       | Tools / Libraries                              |
|----------------|------------------------------------------------|
| Programming    | Python 3.10+                                   |
| Data Handling  | Pandas, NumPy                                  |
| Visualization  | Matplotlib, Seaborn                            |
| Machine Learning | scikit-learn, XGBoost                        |
| Model Persistence | joblib                                       |
| Web Framework  | Flask                                          |
| Frontend       | HTML, CSS, JavaScript                          |
| Development    | Jupyter Notebook, VS Code                      |
| Version Control | Git / GitHub                                  |

---

## Folder Structure

```
Rising-Waters-Flood-Prediction/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── 1. Brainstorming & Ideation/              # Brainstorming and idea prioritization
├── 2. Requirement Analysis/                  # Solution requirements, tech stack, ER diagram
├── 3. Project Design Phase/                  # Data collection, dataset, architecture diagram
├── 4. Project Planning Phase/                # Jupyter notebooks for EDA
├── 5. Project Development Phase/             # Source code and trained models
├── 6. Project Testing/                       # Flask web application and tests
├── 7. Project Documentation/                 # Reports, manuals, guides
├── 8. Project Demonstration/                 # Demo video and presentation
└── assets/                                   # Logos and icons
```

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/AlRihabChandhiniMohammed/rising-waters-flood-prediction.git
   cd rising-waters-flood-prediction
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

   - Activate on Windows: `venv\Scripts\activate`
   - Activate on macOS/Linux: `source venv/bin/activate`

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**

   ```bash
   python "6. Project Testing/app.py"
   ```

   Visit `http://127.0.0.1:5000` in your browser.

---

## Usage

1. Place raw datasets in `3. Project Design Phase/dataset/raw/`.
2. Run the notebooks in `4. Project Planning Phase/notebooks/` in order.
3. Train models using scripts in `5. Project Development Phase/src/`.
4. Launch the Flask app and submit input features via the web interface.
5. View predictions and probability scores on the results page.

---

## Results

| Model          | Accuracy | Precision | Recall | F1-Score |
|----------------|----------|-----------|--------|----------|
| Decision Tree  | 0.9565   | 1.0000    | 0.6667 | 0.8000   |
| Random Forest  | 0.9565   | 1.0000    | 0.6667 | 0.8000   |
| KNN            | 0.9130   | 0.6667    | 0.6667 | 0.6667   |
| XGBoost        | 0.8696   | 0.0000    | 0.0000 | 0.0000   |

---

## Future Scope

- Integrate real-time data from IoT sensors and weather APIs.
- Implement deep learning models (LSTM, GRU) for time-series forecasting.
- Deploy to cloud platforms (AWS, GCP, Azure) with Docker.
- Add geospatial visualization with maps.
- Extend to multi-location and multi-hazard prediction.

---

## Team Members

| Name                          | Role               |
|-------------------------------|--------------------|
| Al Rihab Chandhini Mohammed   | Team Lead          |
| Satyanarayana Akula           | Team Member        |
| Prem Satya Sai Udatha         | Team Member        |
| Ranadeep Vinukonda            | Team Member        |
| Vijay Kiran Kommoju           | Team Member        |

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Project Status and Repository Structure

### Project Status

#### Completed Tasks
- ✅ Entity Relationship Diagram
- ✅ Pre-requisites
- ✅ Project Workflow
- ✅ Epic 1: Data Collection
  - Downloaded the flood prediction dataset.
- ✅ Epic 2: Visualizing and Analysing the Data
  - Importing the required Python libraries.
- ✅ Epic 3: Data Pre-processing
  - Handled outliers using IQR winsorization capping.
  - Implemented encoding check for categorical values.
  - Split dataset into training and test sets using stratified splitting.
  - Applied feature scaling using StandardScaler.
- ✅ Epic 4: Model Building
  - Implemented and tuned Decision Tree Classifier.
  - Implemented and tuned Random Forest Classifier.
  - Implemented and tuned KNN Classifier.
  - Implemented and tuned XGBoost Classifier.
  - Compared the models and selected the best model.
  - Saved the best model in .pkl file.
  

#### Repository Structure

1. **Brainstorming & Ideation/**
   - Brainstorming documents and idea prioritization.

2. **Requirement Analysis/**
   - Requirement analysis documents and project requirements.

3. **Project Design Phase/**
   - Dataset
   - ER Diagram
   - System architecture and design documents.

4. **Project Planning Phase/**
   - Jupyter notebooks for EDA and analysis.
   - flood_prediction_analysis.ipynb

5. **Project Development Phase/**
   - Machine learning source code.
   - Model training scripts.
   - Saved models.

6. **Project Testing/**
   - Flask application.
   - Testing files.

7. **Project Documentation/**
   - Project documentation.
   - Reports.
   - Guides.
   - Tools and libraries documentation.

8. **Project Demonstration/**
   - Presentation.
   - Demo video.
   - Screenshots.

## Project Status by Prem

### Completed Tasks 

* ✅ **Epic 1: Data Collection**

  * Imported the required Python libraries.
  * Loaded the flood prediction dataset into a Pandas DataFrame.
  * Explored the dataset using `head()`, `shape`, `info()`, and `describe()`.
  * Added observations for dataset structure, dimensions, data types, and statistical summary.

* ✅ **Epic 2: Visualizing and Analysing the Data**

  * **Univariate Analysis**

    * Generated distribution plots for all numerical features.
    * Generated box plots to identify data spread and potential outliers.
    * Added observations for each analysis.
  * **Multivariate Analysis**

    * Generated a correlation heatmap to study relationships among features.
    * Added observations highlighting significant feature correlations.
  * **Descriptive Analysis**

    * Performed descriptive statistical analysis using summary statistics.
    * Examined data types and unique values of all features.
    * Documented observations based on the statistical analysis.
  * **Handling Missing Values**

    * Checked for missing values using `isnull().sum()`.
    * Verified the absence of missing values using `isnull().any()`.
    * Confirmed that the dataset contains no missing values and requires no imputation.

* ✅ **Epic 3: Data Pre-processing**

  * Detected and treated outliers using IQR winsorization capping.
  * Checked and encoded categorical columns using one-hot encoding.
  * Split data into stratified training and testing sets.
  * Scaled features using StandardScaler.

* ✅ **Epic 4: Model Building**

  * Built, trained, and tuned Decision Tree Classifier.
  * Built, trained, and tuned Random Forest Classifier.

---

## Repository Structure (Updated)

### Project Planning Phase/

The following notebooks have been completed:

* `01_Data_Collection.ipynb`

  * Dataset loading and initial exploration.

* `02_Univariate_Analysis.ipynb`

  * Distribution plots.
  * Box plots.
  * Observations.

* `03_Multivariate_Analysis.ipynb`

  * Correlation heatmap.
  * Feature relationship analysis.
  * Observations.

* `04_Descriptive_Analysis.ipynb`

  * Descriptive statistics.
  * Data types.
  * Unique value analysis.
  * Observations.

* `05_EDA.ipynb`

  * Missing value detection.
  * Missing value verification.
  * Observations.

---

## Next Tasks

* Continue with KNN and XGBoost model development.
* Implement model comparison script and save the best model.
* Proceed with Flask application development.



# 💧 Rising Waters — Flood Prediction System

> An AI-powered flood risk prediction system built with Machine Learning and a modern web interface.

---

## 📌 Project Overview

Rising Waters combines Machine Learning with a responsive web application to estimate flood risk using real-world environmental data. The trained ML model evaluates ten parameters and predicts whether flood conditions are likely, displaying the result through a clean, modern interface.

**Input Parameters used for prediction:**

| Parameter | Parameter |
|---|---|
| Temperature | Annual Rainfall |
| Humidity | Jan – Feb Rainfall |
| Cloud Cover | Mar – May Rainfall |
| Jun – Sep Rainfall | Oct – Dec Rainfall |
| Average June Rainfall | Sub Divisional Rainfall |

---

## 🚀 Technologies Used

| Layer | Technologies |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python, Flask |
| **Machine Learning** | Scikit-learn, Pandas, NumPy, Pickle |

---

## 📂 Project Structure

```
rising-waters-flood-prediction/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── chance.html
│   └── no_chance.html
│
├── model.pkl
├── app.py
└── README.md
```

---

## ▶️ Running the Project

**1. Clone the repository**

```bash
git clone https://github.com/AlRihabChandhiniMohammed/rising-waters-flood-prediction.git
```

**2. Move into the project folder**

```bash
cd "rising-waters-flood-prediction"
```

**3. Create a virtual environment**

```bash
python -m venv env
```

**4. Activate the environment**

```bash
# Windows
.\env\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the Flask application**

```bash
python "6. Project Testing/app.py"
```

**7. Open in your browser**

```
http://127.0.0.1:5000
```

---

## 💻 Frontend Development

**Developed by Vijay Kiran Kommoju**

### ✅ Contributions

**UI Design & Layout**
- Designed the complete user interface from scratch
- Built a fully responsive layout for desktop, tablet, and mobile devices
- Created a modern landing page with a Hero Section, Feature Cards, Process Flow, and Footer
- Developed the prediction dashboard UI
- Designed the Flood Detected and No Flood result pages

**Design System**
- Glassmorphism card components
- Custom gradient-based color palette using CSS variables
- Smooth animations and scroll reveal effects
- Button ripple effects and loading state animations
- Reusable CSS component architecture

**Functionality & Accessibility**
- Client-side form validation using Vanilla JavaScript
- Semantic HTML5 for better accessibility
- Keyboard focus states and proper ARIA roles
- Integrated frontend with existing Flask backend

---

## 📸 Screenshots

**Home Page**

![Home Page](../rising-waters-flood-prediction/7.%20Project%20Documentation/screenshots/home.png)

**Prediction Form**

![Prediction Form](../rising-waters-flood-prediction/7.%20Project%20Documentation/screenshots/index.png)

**Flood Detected Result**

![Flood Result](../rising-waters-flood-prediction/7.%20Project%20Documentation/screenshots/chance.png)

**No Flood Result**

![Safe Result](../rising-waters-flood-prediction/7.%20Project%20Documentation/screenshots/no_chance.png)