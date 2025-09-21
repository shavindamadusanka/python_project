import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def predict_prices(input_file="./src/data_collection/data/cleaned_books.csv"):
    df = pd.read_csv(input_file)

    X = df[["Rating"]]  # independent variable
    y = df["Price"]     # dependent variable

    model = LinearRegression()
    model.fit(X, y)

    print(f"Model Coefficients: {model.coef_[0]:.2f}, Intercept: {model.intercept_:.2f}")

    # Predict
    predictions = model.predict(X)

    # Plot regression line
    plt.scatter(X, y, label="Actual")
    plt.plot(X, predictions, color="red", label="Predicted")
    plt.xlabel("Rating")
    plt.ylabel("Price (£)")
    plt.title("Linear Regression: Price vs Rating")
    plt.legend()
    plt.show()

def main():
    predict_prices()

if __name__ == "__main__":
    main()
