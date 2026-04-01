from db import fetch_expenses
from analysis import analyze_expenses
from visualize import plot_expenses

def main():
    df = fetch_expenses()

    if df.empty:
        print("No data found!")
        return

    print("\n--- Expense Data ---")
    print(df)

    analyze_expenses(df)
    plot_expenses(df)

if __name__ == "__main__":
    main()
