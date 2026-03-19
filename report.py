import pandas as pd
import matplotlib.pyplot as plt

def generate_report(df):
    # Basic stats
    summary = df.describe()

    # Group analysis
    city_sales = df.groupby('City')['PurchaseAmount'].sum()

    # Plot
    plt.figure()
    city_sales.plot(kind='bar')
    plt.title("Sales by City")
    plt.xlabel("City")
    plt.ylabel("Total Sales")
    plt.savefig("sales_chart.png")

    # Export to Excel
    with pd.ExcelWriter("report.xlsx") as writer:
        df.to_excel(writer, sheet_name="Cleaned Data", index=False)
        summary.to_excel(writer, sheet_name="Summary")
        city_sales.to_frame().to_excel(writer, sheet_name="City Sales")

    print("\nReport generated successfully!")
