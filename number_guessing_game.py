import random
while True:
    val=random.randrange(1,100)
    if(val<30):
        print("Guess number")
        print("Hint:Too Low")
    elif(val>30 and val<60):
        print("Guess number")
        print("Hint:medium")
    else:
        print("Guess number")
        print("Hint:Too high")
    n=int(input())
    if(n==val):
        print("correct")
    else:
        print("wrong")
        print("try it again")
        
