import random
n=random.randint(1,10)
while True:
   x=int(input("Enter your number"))
   if x<n:
       print("Too Low")
   elif x>n:
       print("Too High")
   elif x==n:
       print("You got ur number")
       break
