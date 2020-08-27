#Exercise 2 ~~~~~~~~~~~~~~~~~~FAULTY CALCULATOR~~~~~~~~~~~~~~~~~~~~~

# 45*3 = 555, 56+9 = 77, 56/6 = 4
print("what do u want to do?\n[a]addition\n[b]multiplication\n[c]division")
userinput=input()
if userinput=="a":
    print("enter your first number")
    a=int(input())
    print("enter second number")
    b=int(input())
    if a == 56 and b == 9:
        print(a,"+", b, "=","77")
    elif a == 9 and b == 56:
        print(a, "+", b, "=", "77")
    else:
        print(a, "+", b,"=", a+b)
if userinput=="b":
    print("enter first number")
    a = int(input())
    print("enter second number")
    b = int(input())
    if a == 45 and b == 3:
        print(a, "*", b, "=","555")
    elif a == 3 and b == 45:
        print(a, "*", b, "=", "555")
    else:
        print(a,"*",b,"=",a*b)
if userinput == "c":
    print("enter first number")
    a=int(input())
    print("enter second number")
    b=int(input())
    if a == 56 and b == 6:
        print(a,"/",b,"=","4")
    else:
        print(a,"/",b,"=",a/b)
print("You can trust this calculator completely.")
print(":D")