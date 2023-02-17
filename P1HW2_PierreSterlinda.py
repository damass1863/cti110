# Trip Budget
# 2/16/2023
# CTI-110 P1HW2- Calculate Trip Expense
# Sterlinda Pierre

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas_expenses = float(input("Enter the amount you will spend on gas: "))
accommodation_expenses = float(input("Enter the amount you will spend on accommodation: "))
food_expenses = float(input("Enter the amount you will spend on food: "))
total_expenses = gas_expenses + accommodation_expenses + food_expenses
remaining_budget = budget - total_expenses

print("Your budget for the trip to", destination, "is:", budget)
print("Your total expenses for the trip are:", total_expenses)
print("Your remaining budget for the trip is:", remaining_budget)
