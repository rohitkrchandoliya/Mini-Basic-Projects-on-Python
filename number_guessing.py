print(".....number guessing program  1 to 100 ......")
correct_number=67
user_number=int(input("Enter your number:"))
if(user_number==correct_number):
    print(" congrats! \n you guessed correct number:",user_number)
elif(user_number>=0 and user_number<50):
    print("ohh no! it's too low from the correct number \n your number is:",user_number)
elif(user_number==50):
    print("try again ! you guessed low number\n your number is:",user_number)
elif(user_number>50 and user_number<correct_number):
    print("continue you are progressing for  guess the correct number\n your number is:",user_number)
elif(user_number>correct_number and user_number<75):
    print("shitt! you guessed some high from the correct number \n your number is:",user_number)
elif(user_number>75 and user_number<=100):
    print("you guessed too high! try some low numbers \n your number is:",user_number)
else:
    print("you enterd invalid number:",user_number)