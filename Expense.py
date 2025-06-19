# Expense.py

class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = float(amount)

    def __str__(self):
        return f"{self.name} | {self.category} | ₹{self.amount}"
