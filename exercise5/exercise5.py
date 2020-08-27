#######HEALTH MANAGEMENT SYSTEM#########
# 3 clients - harry rohan hamad
#total 6 files
def getdate():
    import datetime
    return datetime.datetime.now()

#write a function
"""to take input as name"""
#write a function
"""to retrive exercise and food for any client"""
# print(getdate())







print(getdate())
a = int(input("What do you want to do?\n[1] Update diet for today.\n[2] Update exercise.\n"))
if a == 1:
    b = int(input("[1] Harry\n[2] Rohan\n[3]Hamid"))
    if b == 1:
        print("Welcome Harry")
        print(getdate())
        f = open("Harryfood.txt", "r+")
        eaten = input("What did you eat today?")
        f.write(eaten)
        read = f.read()
        print(read)
