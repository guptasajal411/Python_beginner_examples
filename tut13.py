var1 = 6
var2 = 56
#var3 = int(input("enter number"))
#if var3>var2:
#    print(var3, "is greater than", var2)
#elif var3 == var2:
#    print("equal")
#else:
#    print(var3, "is less than", var2)

list1 = [1, 5, 7, 3]
#print(5 not in list1)
"""agar if ke andar ka code true hai toh
indented code execute hota hai"""
#if 5 in list1:
#    print("5 is in the list")
#########QUIZ#########
print("enter your age")
userinput = int(input())
if userinput>18 and userinput<101:
    print("you are eligible to drive")
elif userinput == 18:
    print("come to office")
elif userinput>7 and userinput<18:
    print("you are not eligible to drive")
else:
    print("invalid age group")