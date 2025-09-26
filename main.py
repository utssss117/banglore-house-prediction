from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
pipe = pickle.load(open("model.pkl", "rb"))
data = pd.read_csv("Cleaned_data.csv")

@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations, prediction_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get("location")-
    sqft = float(request.form.get("sqft"))
    bath = float(request.form.get("bath"))
    bhk = float(request.form.get("bhk"))

    input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                            columns=["location", "total_sqft", "bath", "bhk"])

    prediction = pipe.predict(input_df)[0]
    prediction = max(prediction, 0)   # Avoid negative predictions

    result = f"Predicted price for {bhk} BHK in {location} ({sqft} sqft, {bath} bath) is ₹ {round(prediction,2)} Lakhs"

    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations, prediction_text=result)

if __name__ == "__main__":
     
    app.run(debug=True, port=5001, use_reloader=False)
