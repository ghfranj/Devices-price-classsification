import numpy as np
import pandas as pd
import tensorflow as tf

class PricePredictionModel:
    def __init__(self, model_path="saved_model/best_model.h5"):
        self.model = self.load_model(model_path)
        # Extract input shape from the model's first layer
        self.input_shape = self.model.layers[0].input_shape[1:]  # Assuming the first layer is Flatten

    def load_model(self, model_path):
        """Load the trained model from the specified path."""
        model = tf.keras.models.load_model(model_path)
        print(f"Model loaded from {model_path}")
        return model

    def preprocess_input(self, X):
        """Preprocess input data X to match the model's input shape."""
        # Assuming X is a DataFrame or a single sample (numpy array or list)
        if isinstance(X, pd.DataFrame):
            X_processed = X.iloc[:, :self.input_shape[0]].values  # Adjust for actual input shape
        else:
            X_processed = np.array(X)[:, :self.input_shape[0]]  # Adjust for actual input shape

        return X_processed

    def predict_single(self, X):
        """Make a prediction for a single sample."""
        X_processed = self.preprocess_input(X)
        prediction = self.model.predict(X_processed)
        predicted_class = np.argmax(prediction, axis=1)
        return predicted_class

    def predict_group(self, X):
        """Make predictions for a group of samples."""
        X_processed = self.preprocess_input(X)
        predictions = self.model.predict(X_processed)
        predicted_classes = np.argmax(predictions, axis=1)
        return predicted_classes

    def predict_proba(self, X):
        """Make probability predictions on the input data X."""
        X_processed = self.preprocess_input(X)
        return self.model.predict(X_processed)

if __name__ == "__main__":
    # Example usage
    X_test = pd.read_csv("data/X_test_prepared.csv")

    # Initialize the prediction model
    prediction_model = PricePredictionModel()

    # Make predictions for a single sample
    # Assuming X_test_single is a single sample (e.g., first row of X_test DataFrame)
    X_test_single = X_test.iloc[0].values.reshape(1, -1)  # Adjust according to your actual data structure

    # Predictions for single sample
    single_prediction = prediction_model.predict_single(X_test_single)
    print("Single Prediction:", single_prediction)

    # If you need the probabilities for single sample
    single_probability = prediction_model.predict_proba(X_test_single)
    print("Single Prediction Probabilities:", single_probability)

    # Make predictions for a group of samples
    group_predictions = prediction_model.predict_group(X_test)
    print("Group Predictions:", group_predictions)
