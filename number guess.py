#number guessing
import random
secretnumber=random.randint(1,10)
a=int(input("guess a number"))
attempt=0
while a!= secretnumber:
    print("guess not ok ")
    attempt+=1
    if secretnumber>a:
        print("guess higer value")
    else:
        print("guess lower value")
    a=int(input("guess a number"))
else:
    print("guess ok")
    attempt+=1

print("no of attempts",attempt)
print('secret number',secretnumber)