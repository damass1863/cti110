
# A Simple math quiz that allows users to practice addition and subtraction, by generated random numbers.

# 4/27/2023

# CTI-110 P5HW - Math Quiz

# Sterlinda Pierre


import random

def generate_numbers():
    num1 = random.randint(2, 100)
    num2 = random.randint(2, 100)
    return num1,num2

def add_numbers():
    num1, num2 = generate_numbers()
    answer = num1 + num2
    print(f" {str(num1)}")
    print(f"+{str(num2)}")
    return answer

def subtract_numbers():
    num1, num2 = generate_numbers()
    answer = num1 - num2
    print(f" {str(num1)}")
    print(f"-{str(num2)}")
    return answer

def validate_guess(guess, answer):
    if guess == answer:
        print("Congratulations!!!! Your answer is correct.")
        return True
    elif guess < answer:
        print("Sorry, guess is too low.")
    else:
        print("Sorry, guess is too high.")
    return False

print("\nWelcome to Math Quiz \n")

def math_quiz():
    while True:
        print("MAIN MENU")
        print("---------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")
        
        choice = input("Please choose one of the menu options: ")
        
        if choice == "1":
            answer = add_numbers()
        elif choice == "2":
            answer = subtract_numbers()
        elif choice == "3":
            print("\nThank you for playing...Bye!!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            continue
        
        num_guesses = 0
        while True:
            guess = input("\nEnter answer: ")
            num_guesses += 1
            
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please choose one of the menu options.")
                continue
            
            if validate_guess(guess, answer):
                print(f"Number of guesses: {num_guesses}")
                print("\n")
                break
           
if __name__ == "__main__":
    math_quiz()
