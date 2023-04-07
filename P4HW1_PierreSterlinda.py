# CTI-110

# P4HW1 - Score List

# Sterlinda Pierre

# 4/6/2023


#Ask the user to enter the number of scores they want to enter
#Create an empty list to store the scores
#Loop for the number of scores the user wants to enter
#Loop until a valid score is entered
#Ask the user to enter a score
#Check if the score is valid (between 0 and 100)
#If the score is valid, add it to the scores list and exit the inner loop
#If the score is not valid, notify the user and continue the inner loop
#Find the lowest score in the scores list
#Create a modified scores list without the lowest score
#Calculate the average of the modified scores list
#Determine the letter grade for the average
#Display the lowest score, modified score list, average, and letter grade to the user


# Ask user to enter number of scores they would like to enter
num_scores = int(input("How many scores do you want to enter? "))
print("\n")
# Create an empty list to store the scores
scores = []

# Loop to collect the number of scores the user wants to enter
for i in range(num_scores):
    # Loop until a valid score is entered
    while True:
        score = float(input(f"Enter score {i+1}: "))
        if score >= 0 and score <= 100:
            # Add valid score to the scores list and exit the inner loop
            scores.append(score)
            break
        else:
            # Prompt the user to enter a valid score and continue the inner loop
            print("\n")
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

# Find the lowest score
lowest_score = min(scores)

# Create a modified score list without the lowest score
modified_scores = [s for s in scores if s != lowest_score]

# Calculate the average of the modified score list
average = sum(modified_scores) / len(modified_scores)

# Determine the letter grade for the calculated average
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print("\n----------Results--------------")
print(f"Lowest score: {lowest_score}")
print(f"Modified list: {modified_scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade: {letter_grade}")



