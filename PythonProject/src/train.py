import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from data_preparation import prepare_data
from model import DevicePriceClassifier


def main():
    # Paths to the dataset files
    train_path = "data/train - train.csv"
    test_path = "data/test - test.csv"

    # Prepare the data
    X_train, y_train, X_test = prepare_data(train_path, test_path)

    # Split the training data for validation
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

    # Initialize the classifier
    classifier = DevicePriceClassifier(input_shape=(X_train.shape[1],))

    # Train the model
    classifier.train(X_train, y_train, validation_data=(X_val, y_val), epochs=50, batch_size=32)

    # Evaluate the model
    print("Evaluating model on validation data:")
    classifier.evaluate(X_val, y_val)

    # Plot training history
    classifier.plot_training_history()

    # Save the trained model
    model_save_path = "saved_models/device_price_classifier_model.pt"
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    classifier.save_model(model_save_path)


if __name__ == "__main__":
    main()
