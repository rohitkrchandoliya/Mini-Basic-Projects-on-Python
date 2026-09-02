print("......company employees work list ..........")
employees={
"shivam":["analyse company data"],
"Rishi":["check staff problem"],
"Kartik":["create a team for new project"],
"Mira":["check security of company data "],
"Siya":["lead all managers"]
}

e_name=input("Enter your name:")
if (e_name in employees):
   print("yes! you are selected in company\nyour name in list:",e_name)
   while True:
    print("\nHere are Options....\n")
    print("1.check your task")
    print("2.add your task")
    print("3.remove your task")
    print("4.exit")
    choice=int(input("Enter your choice(1/2/3/4):"))
    if(choice==1):
      print("your tasks:",employees[e_name])
    elif(choice==2):
      task=input("enter your new task to Add in list:")
      employees[e_name].append(task)
    elif(choice==3):
      task=input("enter your  task to remove from the list:")
      if(task in employees[e_name]):
        employees[e_name].remove(task)
        print("removed your task from the list:",employees[e_name])
      else:
        print("this task is not find in your list:",task)
    elif(choice==4):
      print("thank you!! for using this project")
      
    else:
      print("wrong choice ")


else:
  print("sorry!!  your name is not in list:",e_name)
