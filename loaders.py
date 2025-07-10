import pandas as pd

def load_csv(path):
    """
    Load data from a CSV file.
    Args:
        path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    return pd.read_csv(path)


def load_ascii(path, colspecs, colnames):
    """
    Load data from a fixed width ASCII file.
    Args:
        path (str): Path to the CSV file.
        colspecs (array-like): Column specifications.
        colnames (array-like): Column names.
    Returns:
        pd.DataFrame: Loaded data.
    """
    return pd.read_fwf(path, colspecs=colspecs, names=colnames)