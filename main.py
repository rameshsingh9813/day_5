from art import *
import random
times=input("Enter the number of time you want to play the game: ")
computer_score=0
Your_score=0
for i in range(int(times)):
  user=int(input("enter the number: "))
  rand_val=random.randint(0,1)
  Art=text2art(f"{rand_val}",font='block')
  Art_1=text2art(f"{user}",font='block')
  print("The computer choice is: ",Art)
  print("Your choice is: ",Art_1)
  if user==rand_val: 
    Your_score+=1
    # print("your scoreis: ",Your_score)
  else:
    computer_score+=1
    # print("computer score is: ",computer_score)
if Your_score>computer_score:
  print("you win by:",Your_score-computer_score)
elif Your_score==computer_score:
  print("match drew")
else:
 print("you lose the match by : ",computer_score-Your_score)