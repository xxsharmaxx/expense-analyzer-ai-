import matplotlib.pyplot as plt

def plot_expenses(df):
    category_sum = df.groupby('category_name')['amount'].sum()

    # Bar Chart
    category_sum.plot(kind='bar', title="Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

    # Pie Chart
    category_sum.plot(kind='pie', autopct='%1.1f%%', title="Expense Distribution")
    plt.ylabel("")
    plt.show()
