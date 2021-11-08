number = int(input("Enter a number: "))
guess = int(500)
print(guess)
while(guess != number):
    isRight = int(input("Enter option: "))
    if(isRight == 1):
        guess = guess - ((1000 - guess)/2)
    if(isRight ==2):
        print("I am right!")
    if(isRight ==3):
        guess = guess + ((1000-guess)/2)
    print(round(guess))
    