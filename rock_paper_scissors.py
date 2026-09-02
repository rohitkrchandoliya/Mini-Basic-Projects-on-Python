
print(".......rock paper scissors game......")
p1=input("enter your turn player 1:")
p2=input("enter your turn player 2:")
if(p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") or(p1=="scissors" and p2=="paper"):
   print("player 1 wins because \n player1 played=",p1,"\n player 2 played=",p2)
else:
   print("player 2 wins because \n player2 played=",p2,"\n player1 played=",p1)