
# CTI-110

# P3HW2 - Salary

# Sterlinda Pierre

# 3/23/2023



# 1. Prompt user to enter employee name
# 2. Prompt user to enter number of hours worked this week
# 3. Prompt user to enter employee's pay rate
# 4. Check if employee worked overtime
# 5. If yes, calculate the amount owed for overtime hours (1.5 times regular rate for each overtime hour)
# 6. Calculate the amount owed for regular hours worked
# 7. Calculate gross pay by adding overtime pay and regular pay
# 8. Display Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay



# Prompt user to enter employee name
employee_name = input("Enter employee's name: ")

# Prompt user to enter number of hours worked this week
hours_worked = float(input("Enter number of hours worked this week: "))

# Prompt user to enter employee's pay rate
pay_rate = float(input("Enter employee's pay rate: "))

print("\n--------------------------------------------------------------------")

# Check if employee worked overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    overtime_pay = 0

# Calculate the amount owed for regular hours worked
regular_pay = (hours_worked - overtime_hours) * pay_rate

# Calculate gross pay by adding overtime pay and regular pay
gross_pay = regular_pay + overtime_pay

# Display Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay


print("Employee name:", employee_name)
print("Hours worked:", hours_worked)
print("Pay rate:", pay_rate)
print("Overtime:", overtime_hours)
print("Overtime pay:", overtime_pay)
print("RegHour pay:", regular_pay)
print("Gross pay:", gross_pay)

