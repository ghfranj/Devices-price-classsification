import os
import numpy as np
import pandas as pd
from model import DevicePriceClassifier
from data_preparation import prepare_input_data
import argparse

def predict(input_data, model_path):
    # Load the trained model
    classifier = DevicePriceClassifier.load_model(model_path)

    # Prepare the input data
    X_input = prepare_input_data(input_data)

    # Predict the price range
    y_prob = classifier.model.predict(X_input)
    y_pred = np.argmax(y_prob, axis=1)
    return y_pred

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Predict device price range.")
    parser.add_argument('input_file', type=str, help="Path to the input CSV file with device specifications.")
    parser.add_argument('model_file', type=str, help="Path to the trained model file.")

    args = parser.parse_args()

    input_file = args.input_file
    model_file = args.model_file

    # Ensure the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} not found.")

    # Ensure the model file exists
    if not os.path.exists(model_file):
        raise FileNotFoundError(f"Model file {model_file} not found.")

    # Read input data
    input_data = pd.read_csv(input_file)

    # Predict the price range
    predictions = predict(input_data, model_file)

    # Add predictions to the input data
    input_data['predicted_price_range'] = predictions

    # Save the predictions to a new CSV file
    output_file = os.path.splitext(input_file)[0] + '_predictions.csv'
    input_data.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")

if __name__ == "__main__":
    main()
