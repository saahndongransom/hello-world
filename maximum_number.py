#comparing three number
num1=int(input("enter a number :"))
num2=int(input("enter  a number :"))
num3=int(input("enter the third number :"))
if (num1>num2):
    if (num1>num3):
        print("num1 is the largest")
    else:
        print("c num3 is the largest")
elif (num2>num3):
        print("num2 is the largest")
else:
        print("num3 is the largest")