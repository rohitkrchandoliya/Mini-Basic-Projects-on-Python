
print("..........check strength of password..........")
all_true_conditions=0
upper=0
lower=0
digit=0
special_symbols=0
# while True:
password=input("Enter your strong password:")
for char in password:
    if(char.isupper()):
        upper=1
    elif(char.islower()):
        lower=1
    elif(char.isdigit()):
        digit=1
    elif(not(char.isalnum())):
        special_symbols=1
    else:
        print("something invalid")
      

if(len(password)>=8):
    all_true_conditions+=1   
    pass
if(upper==1):
    all_true_conditions+=1
    pass
if(lower==1):
    all_true_conditions+=1
    pass
if(digit==1):
    all_true_conditions+=1
    pass
if(special_symbols==1):
    all_true_conditions+=1
    pass
    
           
print("all_true_conditions are:",all_true_conditions)
if(all_true_conditions==5):
    print("superrr!! your password is too strong\n password:",password)
elif(all_true_conditions>=3):
     print("fine!! your password is medium\n password:",password)
else:
     print("sorryyy!! your password is low\n password:",password)