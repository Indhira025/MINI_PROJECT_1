from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open("mini_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        fields = [
            'bedrooms','bathrooms','sqft_living','sqft_lot','floors',
            'waterfront','view','condition','sqft_above','sqft_basement',
            'yr_built','yr_renovated','street','city','statezip',
            'country','Year','Month','Day'
        ]

        values = [float(request.form.get(f, 0)) for f in fields]
        features = np.array([values])

        prediction = model.predict(features)
        price = round(float(prediction[0]), 2)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Price: ₹ {price}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)
