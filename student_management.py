    
print("............Student's Marks Management sheet...............")
fees=15000
attendence=100
subjects=["Hindi","English","Math","Computer","Science"]
students={
    "Rishabh":[[33,89,93,75,67],8000,67],
    "Pawan":[[90,67,88,32,94],6000,78],
    "Priya":[[87,64,98,78,34],9000,89],
    "Akash":[[90,78,76,56,45],12000,93],
    "Shravan":[[90,88,86,30,95],10000,85],
}
s_name=input("Enter your name:")
if (s_name in students):
    print("\nYess!! Student find in Sheet\n Student Name:",s_name)
    while True:
        print("\nYou can check about These---->\n")
        print("\n1.your Marks ,Percentage,Grade,Result(Pass/Fail)")
        print("2.Your  paid ,add  and remain Fee")
        print("3.Your attendence Point(High/Low/Medium)")
        print("4.exit this Sheet")
        choice=int(input("\nEnter your choice for this sheet(1/2/3/4):"))
        if(choice==1):
            for s in students[s_name]:
             if(type(s)==list):
                    while True:
                      Percentage=0
                      print("\nyou can check here:")
                      print("(i).Marks")
                      print("(ii).Perceentage")
                      print("(iii).Grade")
                      print("(iv).Result(Pass/Fail)")
                      print("(v).Exit for here")
                      ch=input("\nEnter your choice(i/ii/iii/iv/v):")
                      if(ch=="i"):
                            print("\nyour subjects:",subjects)
                            print("your Marks:",s)
                      elif(ch=="ii"):
                          marks=0
                          for n in s:
                            marks+=n
                            Percentage=marks*100/500
                          print("\nyour Percentage:",Percentage)
                      elif(ch=="iii"):
                           marks=0
                           for n in s:
                              marks+=n
                           Percentage=marks*100/500
                           if(Percentage>=90 and Percentage<=100):
                               print("\nGrade:A\n")
                               
                           elif(Percentage>=80 and  Percentage<90):
                               print("\nGrade:B\n")
                               
                           elif(Percentage>=70 and  Percentage<80):
                                print("\nGrade:C\n")
                                
                           elif(Percentage>=60 and  Percentage<70):
                                print("\nGrade:D\n") 
                                
                           elif(Percentage>=50 and  Percentage<60):
                               print("\nGrade:D\n")
                                
                           else:
                                print("\nout of Grade\n")
                     
                      elif(ch=="iv"):    
                            for n in s:
                             if(n>=33):
                              print("\npass with numbers:",n)
                             else:
                                print("\nFail with numbers:",n)
                      elif(ch=="v"):
                            print("\nyou are exited from Marks ,Percentage,Grade,Result(Pass/Fail)")
                            break
                            
                      else:
                        print("\nwrong choice")
        elif(choice==2):
                    for s in students[s_name]:
                        if(type(s)==int and s>100):
                         while True:  
                          print("\nCheck Fee Sheet:->\n")
                          print("a Paid Fee")
                          print("b remain fee")
                          print("c add Fee")
                          print("d No need to check(exit)")
                          ch=input("\nEnter  your choice:")
                          if(ch=="a"):
                              print("\nyour paid fees is:",s)
                          elif(ch=="b"):
                              re_f=fees-s
                              print("\nyour remain fees:",re_f)
                          elif(ch=="c"):
                              ad_f=int(input("\nenter your fees to add :"))
                              s+=ad_f
                              students[s_name].insert(1,s)
                              print("\nsuccussfully paid:",ad_f)
                              print("updated fees:",s)
                          elif(ch=="d"):
                              print("\nyou are exited from paid ,add  and remain Fee")
                              break
                              
                          else:
                              print("\nwrong choice")
        elif(choice==3):
                      for s in students[s_name]:
                          if(type(s)==int and s<100 and s>0): 
                              if(s>=80 and s<=100):
                                  print("\nsuperr!! high attendence",s)
                              elif(s>=70 and s<80): 
                                  print("\nfine!!! Medium attendence",s)
                              else:
                                  print("\nSorry!! Low attendence",s) 
        elif(choice==4):
            print("\nyou are exited permanantly from sheet\n ")
            exit()
        else:
            print("\nwrong choice:",5)                                     
else:
    print("\nOops!! no match of this Name:",s_name)