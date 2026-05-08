import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def create_login_dataset():
    """
    Creates a small simulated login dataset.
    Each row represents one login attempt.
    """

    data = [
        # Normal login behaviour
        [9, 0, 1, 0],
        [10, 0, 1, 0],
        [11, 1, 1, 0],
        [13, 0, 1, 0],
        [14, 0, 1, 0],
        [15, 1, 1, 0],
        [16, 0, 1, 0],
        [18, 0, 1, 0],
        [20, 1, 1, 0],
        [21, 0, 1, 0],

        # More normal behaviour
        [8, 0, 1, 0],
        [12, 0, 1, 0],
        [17, 1, 1, 0],
        [19, 0, 1, 0],

        # Suspicious login behaviour
        [3, 6, 5, 1],
        [2, 5, 5, 1],
        [4, 7, 4, 1],
        [23, 4, 5, 1],
    ]

    columns = [
        "login_hour",
        "failed_attempts",
        "country_risk",
        "new_device"
    ]

    return pd.DataFrame(data, columns=columns)


def train_anomaly_model(df):
    """
    Trains an Isolation Forest anomaly detection model.
    The model learns normal behaviour and identifies unusual records.
    """

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    model = IsolationForest(
        contamination=0.20,
        random_state=42
    )

    model.fit(scaled_data)

    predictions = model.predict(scaled_data)

    return predictions


def label_results(df, predictions):
    """
    Isolation Forest returns:
    1 = normal
    -1 = anomaly/suspicious
    """

    df["prediction"] = predictions
    df["result"] = df["prediction"].apply(
        lambda x: "Suspicious" if x == -1 else "Normal"
    )

    return df


def main():
    df = create_login_dataset()

    predictions = train_anomaly_model(df)

    results = label_results(df, predictions)

    results.to_csv("login_anomaly_results.csv", index=False)

    print("AI/ML anomaly detection completed.")
    print("Results saved to login_anomaly_results.csv")
    print()
    print(results)


if __name__ == "__main__":
    main()