
import budget
mybudget = budget.BudgetManager(2500)

print("Total Funds: ", mybudget.funds)

mybudget.addbudget("Books")
mybudget.addbudget("Rent")
mybudget.addbudget("Car note")


mybudget.spend("Books")
mybudget.spend("Rent")
mybudget.spend("Car note")

mybudget.printbudget()


