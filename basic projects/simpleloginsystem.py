attempts = 3
while attempts > 0:
    username = "Abhinavv"
    password = "1234"
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u == username and p == password:
        print("Login successfully")
    else:
        print("invalid username or password")
        attempts = attempts -1
        print("attempts remaining: ",attempts)
    
