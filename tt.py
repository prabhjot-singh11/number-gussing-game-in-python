# name = prabhjot singh
print("=>In this game computer will chosse who play first")
def chose():
    import random
    global players
    players= random.randint(1,2)
    return players
def play1():
 import random
 print(" now player first turn\n")
 n= random.randint(1,100)
 m = int(input("enter a number between 1 to 100\n"))
 
 counter=1
 
 while m!=n:
    if m>n:
        print("imagine small number\n ")
    else:
        print("imagine bigger number\n")
    m= int(input("enter nimber 1 to 100\n"))
    counter+=1
    global d
    d= counter

 else:
    print(f"first player takes {counter} steps\n")

def play2():
 import random
 print(" now secend player turn")
 n= random.randint(1,100)
 m = int(input("enter a number 1 to100\n"))
 counter=1
 while m!=n:
    if m>n:
        print("think small number\n")
    else:
        print(" think bigger number\n")
    m = int(input("enter 1 to 100\n"))
    counter+=1
    global g
    g= counter

 else:
    print(f"secend player takes total {counter} steps")

def com():
    if g>d:
        print(f"player first win the gmae with total {d} steps")
    else:
        print(f"player secend win the game wth total {g} steps")
def main():
    r=chose()
    print(r)
    for i in range(players):
     if r==1:
      play1()
      play2()
      chose()
     if r==2:
      play2()
      play1()
      break    
    com()
    
main()