import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Define constants
TARGET = "classification_diagnostic"
DATAFOLDER = "./data"
int_to_cat = {
    -1: "NaN",
    0: "C2",
    1: "C1",
    2: "C3",
    3: "C4",
    4: "C5"
}

cat_to_int = {v: k for k, v in int_to_cat.items()}

def get_data():
    if not os.path.exists(f"{DATAFOLDER}"):
        os.mkdir(f"{DATAFOLDER}")

    # Load the dataset
    data = pd.read_csv(f"{DATAFOLDER}/sgl-arbres-urbains-wgs84.csv")

    # Split features (X) and target variable (y)
    X = data.drop(columns=[TARGET])  # Features
    y = data[TARGET]  # Target
    y = y.map(cat_to_int).fillna(-1).astype('int8')

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Assign the target variable to the training and testing sets
    X_train[TARGET] = y_train.map(int_to_cat)
    X_test[TARGET] = y_test.map(int_to_cat)

    train_df = X_train
    test_df = X_test

    # Save the training and testing sets to CSV files
    train_df.to_csv(f"{DATAFOLDER}/train.csv")
    test_df.to_csv(f"{DATAFOLDER}/test.csv")

    return train_df, test_df