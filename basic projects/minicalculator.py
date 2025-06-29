a=float(input("enter two numbers: "))
b=float(input())
x=input("enter operation(+,-,*,/):")
if x=="+":
    print("result=",a+b)
elif x=="-":
    print("result=",a-b)
elif x=="*":
    print("result=",a*b)
elif x=="/":
    if b != 0:
        print("result=", a / b)
    else:
        print("division by zero not possible")
else:
    print("invalid operation")
