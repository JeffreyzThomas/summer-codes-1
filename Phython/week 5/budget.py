class BudgetManager:
    def __init__(self, initial_funds):
        self.funds = initial_funds
        self.budgets = {}
        self.expenses = {}

    def add_budget(self, name, amount):
        if name in self.budgets:
            raise ValueError("Cannot add, budget for item exists.")
        if amount > self.funds:
            raise ValueError("No no no, get your money up not your funny up 💲")
        self.budgets[name] = amount
        self.expenses[name] = 0
        self.funds -= amount
        return self.funds

    def spend(self, name, amount):
        if name not in self.expenses:
            raise ValueError("Too far out of fund range.")
        self.expenses[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def print_budget(self):
        print("Budget Item       | Budgeted         | Spent            | Remaining")
        print("--------------------------------------------------------------------------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0

        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenses[name]
            remaining = budgeted - spent
            print(f"{name:<18} ${budgeted:15,.2f} ${spent:15,.2f} ${remaining:15,.2f}")
            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remaining

        print("--------------------------------------------------------------------------")
        print(f"{'Total':<18} ${total_budgeted:15,.2f} ${total_spent:15,.2f} ${total_remaining:15,.2f}")
        print(f"\nRemaining global funds: ${self.funds:,.2f}")
