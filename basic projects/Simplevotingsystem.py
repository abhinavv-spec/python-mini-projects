age = int(input("Enter your age: "))
if age >=18:
    print("you can vote now")
    print("1.candidate1")
    print("2.candidate2")
    vote = int(input("enter your votec(1 or 2): 17"
    ""))
    if vote == 1:
        print("You voted for candidate 1")
    elif vote == 2:
        print("You voted for candidate 2")
    else:
        print("Invalid option")

else:
    print("You cant vote")
