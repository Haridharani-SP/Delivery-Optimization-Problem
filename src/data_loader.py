import pandas as pd

PRIORITY_MAP = {
    "High": 3,
    "Medium": 2,
    "Low": 1
}

def load_data(file_path):
    """
    Load CSV file into pandas DataFrame
    """
    return pd.read_csv(file_path)


def preprocess_data(df):
    """
    Convert priority to numeric and sort data
    """
    df["PriorityValue"] = df["Priority"].map(PRIORITY_MAP)

    df = df.sort_values(
        by=["PriorityValue", "Distance"],
        ascending=[False, True]
    )

    return df