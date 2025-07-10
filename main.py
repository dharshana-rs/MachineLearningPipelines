from loaders import load_csv
from cleaners import clean_data


def run_pipeline():
    df = load_csv("./data/data.csv")
    df_clean = clean_data(df)
    print(df_clean.head())

if __name__ == "__main__":
    run_pipeline()
