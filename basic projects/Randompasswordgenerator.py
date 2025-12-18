import random
characters ="qwertyuioplkjhgfdsazxcvbnm@#$QWERTYUIOPLKJHGFDSAZXCVBNM1234567890"
length = int(input("Enter the length of password: "))
password = " "
for i in range(length):
    password += random.choice(characters)
print("Generated password is:",password)

