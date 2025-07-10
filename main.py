from loaders import load_csv, load_ascii
from cleaners import clean_data
import argparse


def run_pipeline(csv_path: str, ascii_path: str):
    print("\nCSV Files")
    df = load_csv(csv_path)
    df_clean = clean_data(df)
    print(df_clean.head())

    print("\nASCII Files")
    colspecs = [(0, 2), (2, 12), (12, 24)]
    colnames = ["id", "job_title", "location"]
    df_fwf = load_ascii(ascii_path, colspecs, colnames)
    df_fwf_clean = clean_data(df_fwf)
    print(df_fwf_clean.head())


def parse_args():
    parser = argparse.ArgumentParser(description="Run data pipeline for CSV and ASCII files.")
    parser.add_argument(
        "--csv",
        type=str,
        default="./data/data.csv",
        help="Path to the CSV file",
    )
    parser.add_argument(
        "--ascii",
        type=str,
        default="./data/data_ascii.txt",
        help="Path to the ASCII (fixed-width) file",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_pipeline(args.csv, args.ascii)
