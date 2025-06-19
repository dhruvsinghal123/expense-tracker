from Expense import Expense

def main():
    print("💸 Running Expense Tracker")
    expenses_path = "expenses.csv"

    # Ask user for total budget
    total_budget = float(input("Enter your total budget (₹): "))

    # Get input for a new expense
    expense = get_user_expenses()
    print("\n✅ Expense recorded:", expense)

    # Save expense to file
    save_expenses_to_file(expense, expenses_path)

    # Read and summarize expenses
    expenses = summarize_expenses(expenses_path)

    # Show remaining budget
    show_remaining_budget(total_budget, expenses)


def get_user_expenses():
    print("\n📥 Getting user expenses")
    expense_name = input("Enter the expense name: ")
    expense_amount = input("Enter the expense amount (₹): ")

    expense_categories = ["🍔 Food", "🏠 Home", "🏢 Work", "🎉 Fun", "🎤 Misc"]
    while True:
        print("\nSelect a category:")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        selected_index = int(input("Enter the category number: ")) - 1
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name,
                category=selected_category,
                amount=float(expense_amount)
            )
            return new_expense
        else:
            print("❌ Invalid category. Please try again.")


def save_expenses_to_file(expense: Expense, expenses_path):
    print(f"\n💾 Saving expense to '{expenses_path}'...")
    with open(expenses_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expenses(expenses_path):
    print("\n📊 Summary of All Expenses:")
    expenses = []
    with open(expenses_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            try:
                expense_name, expense_category, expense_amount = line.strip().split(",")
                line_expense = Expense(
                    name=expense_name,
                    amount=float(expense_amount),
                    category=expense_category
                )
                print(line_expense)
                expenses.append(line_expense)
            except ValueError:
                print(f"⚠️ Skipping invalid line: {line.strip()}")

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("\n💰 Total by Category:")
    for category, total in amount_by_category.items():
        print(f"{category}: ₹{total:.2f}")
    
    return expenses


def show_remaining_budget(total_budget, expenses):
    total_spent = sum(exp.amount for exp in expenses)
    remaining = total_budget - total_spent
    print(f"\n💰 Total Spent: ₹{total_spent:.2f}")
    print(f"💵 Remaining Budget: ₹{remaining:.2f}")


if __name__ == "__main__":
    main()
