
print(".......trying to create shapes......")
rows=8
cols=8
symbol=input("enter your symbol:")
shape=input("enter your shape:")
how_many=int(input("enter the number of shapes:"))
for shape_count in range(how_many):
 if(symbol=="*" and shape=="traingle") and (how_many>0 and how_many<=10):
    for i in range(1,7):
        print("\n")
        for j in range(i-1,6):
            print("*  ",end="\t")
            
 elif(symbol=="*" and shape=="square") and (how_many>0 and how_many<=10):
    
        for i in range(rows):
            for j in range(cols):
              if(i==0 or i==rows-1) or (j==0 or j==cols-1):
                print("*  ",end="")
              else:
                  print("   ",end="")
            print()
        print()
        
 else:
    print("something error")





print(".......word conversion in english...........")
dic={
    "kursi":"chair",
    "kaichi":"scissors",
    "mej":"table",
    "bistar":"bed",
    "chaku":"knife"
}
word=input("Enter your word for conversion:")
print("in english",word,"is called:",dic[word])









   






    
    
    





    


