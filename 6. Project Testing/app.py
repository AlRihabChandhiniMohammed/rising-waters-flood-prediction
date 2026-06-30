from flask import Flask, render_template, request, redirect, url_for
import os
import joblib
import pandas as pd

app = Flask(__name__)

# -------------------------------------------------
# Load trained model and scaler
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "5. Project Development Phase",
    "models",
    "best_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "5. Project Development Phase",
    "models",
    "scaler.pkl"
)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# -------------------------------------------------
# Routes
# -------------------------------------------------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict_page():
    return render_template("index.html")


@app.route("/chance")
def chance():
    return render_template("chance.html")


@app.route("/no_chance")
def no_chance():
    return render_template("no_chance.html")


# -------------------------------------------------
# Prediction
# -------------------------------------------------

@app.route("/predict_flood", methods=["POST"])
def predict_flood():
    

    try:
        temp = float(request.form["temp"])
        humidity = float(request.form["humidity"])
        cloud = float(request.form["cloud"])
        annual = float(request.form["annual"])
        janfeb = float(request.form["janfeb"])
        marmay = float(request.form["marmay"])
        junsep = float(request.form["junsep"])
        octdec = float(request.form["octdec"])
        avgjune = float(request.form["avgjune"])
        subdivision = float(request.form["sub"])

        data = pd.DataFrame([[
            temp,
            humidity,
            cloud,
            annual,
            janfeb,
            marmay,
            junsep,
            octdec,
            avgjune,
            subdivision
        ]], columns=[
            "Temp",
            "Humidity",
            "Cloud Cover",
            "ANNUAL",
            "Jan-Feb",
            "Mar-May",
            "Jun-Sep",
            "Oct-Dec",
            "avgjune",
            "sub"
        ])

        scaled = scaler.transform(data)

        prediction = model.predict(scaled)[0]

        confidence = None

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(scaled)[0]
            confidence = round(max(probabilities) * 100, 2)

        if prediction == 1:
            return render_template("chance.html", confidence=confidence)
        else:
            return render_template("no_chance.html", confidence=confidence)

    except Exception as e:
        return f"Error : {e}"


# -------------------------------------------------
# Run Application
# -------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)