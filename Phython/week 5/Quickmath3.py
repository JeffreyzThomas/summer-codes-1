class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero"
  
    def subtract(self, a, b):
        return a - b

my_calculator = Calculator()

sum_result = my_calculator.add(10, 5)
product_result = my_calculator.multiply(10, 5)
quotient_result = my_calculator.divide(10, 5)
difference_result = my_calculator.subtract(10, 5)

print("Sum:", sum_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Difference:", difference_result)