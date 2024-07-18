import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def load_data(train_path, test_path):
    """Load the train and test datasets."""
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df


def handle_missing_values(df):
    """Handle missing values in the dataset."""
    # Using SimpleImputer to fill missing values
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    return df_imputed


def feature_engineering(df):
    """Apply feature engineering techniques."""
    # Example: Create pixel density feature
    df['px_density'] = df['px_width'] * df['px_height']
    return df


def scale_features(train_df, test_df):
    """Scale numerical features using StandardScaler."""
    scaler = StandardScaler()
    features = train_df.columns.difference(['price_range'])
    train_df[features] = scaler.fit_transform(train_df[features])
    test_df[features] = scaler.transform(test_df[features])
    return train_df, test_df


def prepare_data(train_path, test_path):
    """Main function to prepare the data."""
    # Load data
    train_df, test_df = load_data(train_path, test_path)

    # Handle missing values
    train_df = handle_missing_values(train_df)
    test_df = handle_missing_values(test_df)

    # Feature engineering
    train_df = feature_engineering(train_df)
    test_df = feature_engineering(test_df)

    # Scale features
    train_df, test_df = scale_features(train_df, test_df)

    # Split features and target for training data
    X_train = train_df.drop(columns=['price_range'])
    y_train = train_df['price_range']

    return X_train, y_train, test_df


if __name__ == "__main__":
    train_path =  "data/train - train.csv"
    test_path =  "data/test - test.csv"

    X_train, y_train, X_test = prepare_data(train_path, test_path)

    # Save prepared data
    X_train.to_csv("data/X_train_prepared.csv", index=False)
    y_train.to_csv("data/y_train_prepared.csv", index=False)
    X_test.to_csv("data/X_test_prepared.csv", index=False)
    print("Done with data preparation")
