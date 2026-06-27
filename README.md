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
├── Brainstorming & Ideation/                 # Brainstorming and idea prioritization
├── Requirement Analysis/                     # Solution requirements and tech stack
├── Project Design Phase/                     # Data collection, ERD, architecture
├── Project Planning Phase/                   # Jupyter notebooks for EDA
├── Project Development Phase/                # Source code and trained models
├── Project Testing/                          # Flask web application and tests
├── Project Documentation/                    # Reports, manuals, guides
├── Project Demonstration/                    # Demo video and presentation
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
   python "Project Testing/app.py"
   ```

   Visit `http://127.0.0.1:5000` in your browser.

---

## Usage

1. Place raw datasets in `Project Design Phase/dataset/raw/`.
2. Run the notebooks in `Project Planning Phase/notebooks/` in order.
3. Train models using scripts in `Project Development Phase/src/`.
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
