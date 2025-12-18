#for basic studies only
mark1 = int(input("Enter first mark(out of 100): "))
mark2 = int(input("Enter second mark(out of 100): "))
mark3 = int(input("Enter third marks(out of 100): "))
average = (mark1 + mark2 + mark3)/3
if average >= 90 :
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print ("Grade C")
else: print ("Failed")
