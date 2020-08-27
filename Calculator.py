india=input("What do you want to do?\n[a]sum of two numbers\n[b]multipliction of two numbers\n[c]division of two numbers\n[d]check if your number is even or odd\n\n")
if india=="a":
    no1=int(input("enter your first number  "))
    no2=int(input("enter your second number  "))
    c=no1+no2
    print(no1,"+",no2,"=",c)
if india=="b":
    no1 = int(input("enter your first number  "))
    no2 = int(input("enter your second number  "))
    c = no1*no2
    print(no1,"*",no2,"=",c)
if india=="c":
    no1 = int(input("enter your first number  "))
    no2 = int(input("enter your second number  "))
    c = no1/no2
    print(no1,"/",no2,"=",c)
if india == "d":
        no1 = int(input("enter your number  "))
        c=no1%2
        if c==0:
            print(no1,"is an even number.")
        else:
            print(no1,"is an odd number")
else:
    print("Please select one of the given operations.")

print("Thank you.")