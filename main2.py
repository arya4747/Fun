import random

computer= random.choice([1,-1,0])
print("'Stone: s'\n'Paper: p'\n'Scissors: z'")
ustr=input("Enter your choice: ")
uDict={"s":1, "p":-1, "z":0}
cdict={1:"Stone", -1:"Paper", 0:"Scissors"}

u=uDict[ustr]

print(f"'You choose: {cdict[u]}'\n'Computer choose: {cdict[computer]}'")

if(computer == u):
    print("It's a Draw")
else:
    if((computer - u == 2) or (computer - u == -1)):
        print("You win!")
    else:
        print("Computer Win!")