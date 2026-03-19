from cleaning import clean_data
from report import generate_report

def run_pipeline():
    file_path = "raw_data.csv"

    # Step 1: Clean Data
    cleaned_df = clean_data(file_path)

    # Step 2: Generate Report
    generate_report(cleaned_df)

if __name__ == "__main__":
    run_pipeline()
