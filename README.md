# Bengaluru House Price Prediction

This project is a web application that predicts house prices in Bengaluru using machine learning. The app is built with Flask and uses a trained Ridge Regression model to estimate prices based on user input.

## Features
- Predict house prices based on location, square footage, number of bedrooms (BHK), and bathrooms
- Cleaned and preprocessed real-world Bengaluru housing data
- Interactive web interface with modern UI (Bootstrap)
- Model training and retraining scripts included

## Project Structure
```
├── bengaluru_house_prices.csv      # Raw dataset
├── cleaned_data.csv                # Cleaned dataset after preprocessing
├── bng.ipynb                       # Jupyter notebook for data analysis & model development
├── train_model.py                  # Script to train and save the ML model
├── model.pkl                       # Trained Ridge Regression model (pickle)
├── RidgeModel.pkl                  # Alternative model (joblib)
├── main.py                         # Flask web application
├── static/
│   └── bg.jpg                      # Background image for UI
├── templates/
│   └── index.html                  # HTML template for the web app
```

## How to Run
1. **Install dependencies**
   ```bash
   pip install flask pandas scikit-learn
   ```
2. **Train the model (optional)**
   If you want to retrain the model:
   ```bash
   python train_model.py
   ```
3. **Start the Flask app**
   ```bash
   python main.py
   ```
   The app will run at [http://localhost:5001](http://localhost:5001)

4. **Open in browser**
   Go to [http://localhost:5001](http://localhost:5001) and use the form to predict house prices.

## Data Source
- The dataset is based on real Bengaluru house prices and includes features like location, size, number of bathrooms, and more.

## Notebooks
- `bng.ipynb` contains the full data cleaning, feature engineering, and model training workflow.

## License
This project is for educational purposes.
