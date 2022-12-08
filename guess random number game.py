import random
x,y=input("enter the range:").split(',')
a=int(x)
b=int(y)
rad=random.randint(a,b)
actual_number=rad
print("random number is:",actual_number)
attempts = 0
p=0
while attempts<3:
    attempts=attempts+1
    guess = int(input("Guess the number:"))
    if guess<actual_number and attempts<3:
        print("Have one more try`.Your guess was too low.")
        print()

    elif (guess > actual_number) and (attempts<3):
        print("Have one more try.Your guess was too high.")

    elif (guess < actual_number) and (attempts ==3):
        print("your last try is finished.Your guess was too low.")

    elif (guess > actual_number) and (attempts == 3):
        print("your last trial has finished.Your guess was too high.")

    else:
        print("You gussed the correct number in {} attempts".format(attempts))
        p=p+1
        if(p==1 and (attempts==2 or attempts==1)):
            actual_number = random.randint(a, b)
            print("new random number is:", actual_number)
        elif(p==2 and (attempts==2 or attempts==1)):
            actual_number=random.randint(a, b)
            print("new random number is:",actual_number)
        else:
            print("you are the winner")

    print("your points are:",p)
print("thank for playing!")
