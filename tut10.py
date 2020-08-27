#Dictionary
d1 = {}
#print(type(d1))
d2 = {"sajal":"roti", "fittuber":"vegan", "ranveer":"eggs",
      "akshay":{"b":"poha", "l":"andaa", "d":"protein"}}
#d2["agurav"] = "sabji"
#d2["arpit"] = "idli"
#print(d2["akshay"]["l"])
#print(d2["arpit"])
#del d2["agurav"]
#print(d2)
d3 = d2.copy()
del d3["sajal"]
#print(d3)
d2.update({"lekha":"kela"})
#print(d2)
#print(d2.keys())
#print(d2.items())
###############EXERCISE################
dict = {"Sajal":"Moist",
        "Shraddha":"Astha",
        "Shanti":"Peace",
        "Kavita":"Poem"}
print("search the dictionary")
userinput = input()
caps = userinput.capitalize()
print(dict[caps])