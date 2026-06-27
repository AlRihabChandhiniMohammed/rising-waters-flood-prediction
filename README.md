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

<!-- TODO: Add model performance comparison table and screenshots -->

| Model          | Accuracy | Precision | Recall | F1-Score |
|----------------|----------|-----------|--------|----------|
| Decision Tree  | —        | —         | —      | —        |
| Random Forest  | —        | —         | —      | —        |
| KNN            | —        | —         | —      | —        |
| XGBoost        | —        | —         | —      | —        |

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
