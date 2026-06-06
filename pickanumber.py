# pick a number game from 100 days of python
list= range(1,101)
import random
c = int(random.choice(list))
ui = random.choice(list)
dl="easy"
if dl=="easy":
  print("numberofattempts=10")
if dl=="hard":
   print("numberofattempts=5")
while dl=="easy":
 nat=10
 while nat!= 0:
   if ui in range(c-5,c+5):
    print(" u are a lil close")
    nat-= 1
   elif ui in range(c-10,c+10):
     print('u are far')
     nat-= 1
   elif ui==c:
      print("hooray u won the game!!!")
   else:
     print('u are too far')
     nat-= 1
while dl=="hard":
 nat=5
 while nat!=0:
   if ui in range(c-5,c+5):
    print(" u are a lil close")
    nat-= 1
   elif ui in range(c-10,c+10):
     print('u are far')
     nat-= 1
   elif ui==c:
      print("hooray u won the game!!!")
   else:
     print('u are too far')
     nat-= 1
