# CTI-110

# P2HW2 - List

# Sterlinda Pierre

# 3/9/2023

# 1. Initialize an empty list to store grades
# 2. Ask the user to enter grades for each module and append it to the list
# 3. Calculate the lowest grade in the list using the min() function
# 4. Calculate the highest grade in the list using the max() function
# 5. Calculate the sum of grades in the list using the sum() function
# 6. Calculate the average grade by dividing the sum by the number of grades
# 7. Display the lowest grade, highest grade, sum of grades, and average grade with two decimal positions


grades = []
for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades.append(grade)
    
# Find the lowest grade, highest grade, sum, and average

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)   

# Display the results
print("\n----------Results--------------")

print(f"Lowest grade: {lowest}")
print(f"Highest grade: {highest}")
print(f"Sum of grades: {total}")
print(f"Average: {average:.2f}")
