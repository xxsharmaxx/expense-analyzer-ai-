def analyze_expenses(df):
    print("\n--- Expense Analysis ---")

    total = df['amount'].sum()
    print(f"Total Expense: ₹{total}")

    category_sum = df.groupby('category_name')['amount'].sum()

    print("\nCategory-wise Spending:")
    print(category_sum)

    # AI Suggestion Logic
    print("\n--- AI Suggestions ---")

    highest = category_sum.idxmax()

    print(f"You are spending the most on: {highest}")

    if highest == "Food":
        print("Try reducing outside food expenses.")
    elif highest == "Shopping":
        print("Control unnecessary shopping.")
    elif highest == "Entertainment":
        print("Limit entertainment expenses.")

    # Prediction (simple)
    avg = df['amount'].mean()
    predicted = avg * 30
    print(f"\nEstimated next month expense: ₹{round(predicted,2)}")
