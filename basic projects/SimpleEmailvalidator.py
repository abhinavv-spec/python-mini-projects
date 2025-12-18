email = input("Enter your email id:")
if "@" in email and "." in email and email.index("@") < email.index(".") and " " not in email:
    print("valid email")
else:
    print("invalid email")
