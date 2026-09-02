print("..............matching password and user for login............")
correct_user="priyanshi"
correct_password="8967pri"
for i in range(1,4):
   try_user=input("Enter user:")
   try_password=input("Enter password:")
   if(try_user==correct_user and try_password==correct_password):
    print(" congrats login successfully !")
   else:
    print("wrong user or wrong password ,\n you have ",3-i,"chance for enter correct user and password")
print("get lost from here")
