
import random

print("Time for toss, Enter 0 for Heads and 1 for Tails")
choice = int(input("Your choice: "))
coin = random.randint(0, 1)

if coin == choice:
    print("You have won the toss")
    print("Select 0 to bat, 1 to bowl ")
    player = int(input("Your choice: "))
    if player == 1:
        print("You chose to bowl")
        u = 1
        com = 0
    else:
        print("You chose to bat")
        u = 0
        com = 1
else:
    print("Computer won the toss")
    player = random.randint(0, 1)
    if player == 1:
        print("Computer chose to bat")
        com = 2
        u = 3
    else:
        print("Computer chose to bowl")
        com = 3
        u = 2

if (u == 1) or (com == 2):
    print("Enter numbers between 1 and 6. If same number, computer is out")
    ctotal = utot = 0
    cs = us = 0

    while cs == 0:
        unum = int(input("Enter your number to bowl: "))
        cnum = random.randint(1, 6)
        print("User chose", unum)
        print("Computer chose", cnum)
        if unum > 6 or unum <= 0:
            print("Invalid number")
            continue
        if unum == cnum:
            print("Computer is out")
            cs = 1
        else:
            ctotal += cnum
            print("Computer score:", ctotal)

    print("Computer final score:", ctotal)

    while us == 0:
        unum = int(input("Enter your number to bat: "))
        cnum = random.randint(1, 6)
        print("User chose", unum)
        print("Computer chose", cnum)
        if unum > 6 or unum <= 0:
            print("Invalid number")
            continue
        if unum == cnum:
            print("You are out")
            us = 1
        else:
            utot += unum
            print("Your score:", utot)
        if utot > ctotal:
            break

    print("Your final score:", utot)

else:
    print("Enter numbers between 1 and 6. If same number, you are out")
    ctotal = utot = 0
    cs = us = 0

    while us == 0:
        unum = int(input("Enter your number to bat: "))
        cnum = random.randint(1, 6)
        print("User chose", unum)
        print("Computer chose", cnum)
        if unum > 6 or unum <= 0:
            print("Invalid number")
            continue
        if unum == cnum:
            print("You are out")
            us = 1
        else:
            utot += unum
            print("Your score:", utot)

    print("Your final score:", utot)

    while cs == 0:
        unum = int(input("Enter your number to bowl: "))
        cnum = random.randint(1, 6)
        print("User chose", unum)
        print("Computer chose", cnum)
        if unum > 6 or unum <= 0:
            print("Invalid number")
            continue
        if unum == cnum:
            print("Computer is out")
            cs = 1
        else:
            ctotal += cnum
            print("Computer score:", ctotal)
        if ctotal > utot:
            break

    print("Computer final score:", ctotal)

if utot > ctotal:
    print("You won")
elif utot == ctotal:
    print("Tie")
else:
    print("You lost")
