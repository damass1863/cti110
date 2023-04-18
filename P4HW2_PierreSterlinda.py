# CTI-110

# P4HW2 - Salary Calculator

# Sterlinda Pierre

# 4/17/2023


# 1. Initialize variables for overtime total, regular pay total, gross pay total, and number of employees entered.
# 2. Begin a while loop that continues until the user enters "Done" for the employee name.
# 3. Prompt the user to enter the employee name and store it in a variable "employee_name".
# 4. Prompt the user to enter the number of hours worked by the employee and store it in a variable "hours_worked".
# 5. Prompt the user to enter the pay rate of the employee and store it in a variable "pay_rate".
# 6. If hours_worked is greater than 40, then calculate overtime hours by subtracting 40 from hours_worked and store it in a variable "overtime_hours". Else, set overtime_hours to 0.
# 7. Calculate the amount owed for overtime hours by multiplying overtime_hours by 1.5 times the pay_rate and store it in a variable "overtime_pay".
# 8. Calculate the amount owed for regular hours by multiplying (hours_worked - overtime_hours) by pay_rate and store it in a variable "regular_pay".
# 9. Calculate the gross pay by adding overtime_pay and regular_pay and store it in a variable "gross_pay".
# 10. Add the overtime_pay, regular_pay, and gross_pay to their respective total variables.
# 11. Increment the number of employees entered by 1.
# 12. Prompt the user to enter another employee's name or enter "Done" to terminate the program.
# 13. Once the user has entered "Done", display the following details: number of employees entered, total amount paid for overtime, total amount paid for regular pay, and total amount paid for all employees.

overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0
overtime_hours = 0
overtime_pay = 0
regular_pay = 0
gross_pay = 0

# Begin while loop
while True:
    # Prompt user to enter employee name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    # Display results
    
    if employee_name == 'Done':
        print("Total number of Employees Entered: ", num_employees)
        print("Total amount paid for overtime : $", overtime_total)
        print("Total amount paid for regular hours: $", regular_pay_total)
        print("Total amount paid in gross: $", gross_pay_total)
        break
        print('\n')

    # Prompt user to enter number of hours worked this week
    
    hours_worked = float(input("How many hours does " + employee_name + " work? "))
    
    # Prompt user to enter employee's pay rate
    pay_rate = float(input("What is " + employee_name + "'s pay rate? "))
       
    # Determine overtime hours and calculate overtime pay if necessary
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        overtime_pay = 0

    # Calculate regular pay
    regular_pay = (hours_worked - overtime_hours) * pay_rate

    # Calculate gross pay
    gross_pay = overtime_pay + regular_pay

    # Add to total variables
    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay
    num_employees += 1


    # Display Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay
    print('\n')

    print("Employee name:", employee_name)
    
    print('\n')

    print("hours_worked   pay_rate  overtime  overtime_pay  regular_pay  gross_pay")
    print("-------------------------------------------------------------------------------")
    
    print(f'{hours_worked:<15.2f} {pay_rate: <10.2f} {overtime_hours:<10.1f} {overtime_pay:<10.2f} ${regular_pay:<10.2f} ${gross_pay:<10.2f}')
    print('\n')

    
