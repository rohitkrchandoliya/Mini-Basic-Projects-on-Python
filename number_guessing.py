
print(".....Number Guessing Program (1 to 100).....")

correct_number = 67

while True:
    try:
        user_number = int(input("Enter your number (1-100): "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    if user_number < 1 or user_number > 100:
        print("Invalid number! Choose a number between 1 and 100.")

    elif user_number == correct_number:
        print("Congrats! You guessed the correct number:", user_number)
        break

    elif user_number < correct_number:
        print("Too low! Try a higher number.")

    else:
        print("Too high! Try a lower number.")
