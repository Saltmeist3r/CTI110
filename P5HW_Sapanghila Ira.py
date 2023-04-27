import random
print("#MathQuiz\n#April 27,2023\n#CTI-110 P5HW - Math Quiz\n#Ira Chriel Sapanghila\n#")
def main():
    while True:
        print("\nWelcome to Math Quiz\n")
        print("MAIN MENU")
        print("-------------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        choice = input("\nPlease choose one of the menu options: ")
        if choice == "1":
            add_quiz()
        elif choice == "2":
            sub_quiz()
        elif choice == "3":
            print("Thank you for playing!!!!\nBye!!")
            break
        else:
            print("Invalid choice. Please choose a number from the menu.")

def add_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = num1 + num2
    guess = None
    num_guesses = 0
    first_guess = True
    
    print(f"  {num1}\n+ {num2}")
    
    while guess != answer:
        if first_guess:
            guess = input("Enter answer.\n")
            first_guess = False
        else:
            guess = input("Try again: ")
        num_guesses += 1
        
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess < answer:
            print("Sorry, guess is too low.\n")
        elif guess > answer:
            print("Sorry, guess is too high.\n")
    
    print("Congratulations!!!! Your answer is correct.")
    print("Number of guesses: ", num_guesses)
    

def sub_quiz():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, num1)
    answer = num1 - num2
    guess = None
    num_guesses = 0
    first_guess = True
    
    print(f"  {num1}\n- {num2}")
    
    while guess != answer:
        if first_guess:
            guess = input("Enter your answer: ")
            first_guess = False
        else:
            guess = input("Try again: ")
        num_guesses += 1
        
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess < answer:
            print("Sorry, guess is too low.\n")
        elif guess > answer:
            print("Sorry, guess is too high.\n")
            
    print("Congratulations!!!! Your answer is correct.")
    print("Number of guesses: ", num_guesses)
    

if __name__ == "__main__":
    main()
