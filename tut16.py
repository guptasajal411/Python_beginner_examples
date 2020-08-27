list1 = [["sajal", 1], ["shraddha",2], ["shanti",3], ["kavita",4]]
dict1 = dict(list1)
#print(dict1)
#for item, lollypop in dict1.items():
    #print(item, lollypop)
#for item in dict1:
    #print(item)
##################QUIZ#################
list2 = ["sajal", 1, 2, 3, 4, 5, 6, 8, 9, 44, 5.5,
         "shanti", "syrotech"]
for item in list2:
    if type(item) == int:
        if item >= 6:
            print(item)