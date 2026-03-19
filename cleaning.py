import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    print("Original Data:\n", df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df['City'] = df['City'].fillna("Unknown")
    df['PurchaseAmount'] = df['PurchaseAmount'].fillna(df['PurchaseAmount'].median())

    # Standardize text
    df['Name'] = df['Name'].str.strip().str.title()
    df['City'] = df['City'].str.strip().str.title()

    print("\nCleaned Data:\n", df)

    # Save cleaned data
    df.to_csv("cleaned_data.csv", index=False)

    return df
