def clean_data(df):
    """
    Clean the DataFrame.
    Args:
        df (pd.DataFrame): Raw data.
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Example logic
    df = df.dropna()
    return df