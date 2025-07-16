funds = 2400000000000000
budgets = {}
expenses = {}
def addbudget(name, amount):
     global funds
     if name in budgets:
          raise ValueError("Cannot add, budget for item exists")
     if amount > funds:
          raise ValueError("No no no, get your money up not your funny up💲 ")
     budgets[name] = amount
     funds = funds - amount
     #or funds -= amount
     expenses[name] = 0
     return funds 
def gone(name, amount):
    if name not in expenses:
         raise ValueError("Too far out of fund range")
    expenses[name] += amount#add exspenses
    budgeted = budgets[name]
    gone = expenses[name]
    return budgeted - gone
 
def printBudget():
    print("budget           Budgeted               Spent               Remaining")
    print("-----------------------------------------------------------------------")
    totalbudgeted = 0
    totalspent = 0
    totalremaining = 0
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingB = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}'  f'{remainingB:10.2f}')
        totalbudgeted += budgeted
        totalspent += spent
        totalremaining += remainingB
    print(f'{"Total":15s}, {totalbudgeted:10.2f}, {totalspent:10.2f}'f'{totalbudgeted-totalspent:10.2f}')
#print("Total funds", funds)
#print((addbudget"Cyberpunk dlc and Edge runners props", 250))
#print((gone"controlers", 50))
#print(budgets)
#print(expenses)
#print(funds)

print("Total funds:", funds)
addbudget("Cyberpunk dlc", 100)
addbudget("Sandevistand", 50000000)
addbudget("Beanies", 140)


gone("Cyberpunk dlc", 100)
gone("Sandevistand", 500000)
gone("Beanies", 140)

printBudget()