# how to create and print dictionary

dic = {
    'name':'afsan',
    'surname':'khan',
    'age':29

}

print(dic) # to access the full elemen from the dic

print(dic['name']) # to get the value of the particular keys in the dic

# get() method --> this is also used to return value of the particular key

print(dic.get('surname'))

#change the vlaues of the particular key

dic['name'] = "Salman"
print(dic)

# loop through a dic
for x in dic:  # loop through keys
    print(x)  # this will lopp through all the keys and only displays the key
    print(dic[x]) # this will  display the values

for x in dic.values(): # loop through values
    print(x)

for x,y in dic.items(): # loop through keys and values
    print(x,y)  # x will store the keys where y will store a values


# adding element in a dic
dic['language'] = "Hindi"
print(dic)

# removing items from a dictinoary

dic.pop('language')
print(dic)

dic.popitem() # removes the last element from the dic
print(dic)

dic2 = {
    "gender":"male",
    "job":"data scientist",
    "domain":"python developer"
}

# del

del dic2["domain"]
print(dic2)

# del also deletes the particular dic
try:
    del dic2
    print(dic2)
except NameError:
    print("there is no dic present as u deleted")

dic2 = {
    "gender":"male",
    "job":"data scientist",
    "domain":"python developer"
}

# clear

dic2.clear() # this will clear the dic
print(dic2)

dic2 = {
    "gender":"male",
    "job":"data scientist",
    "domain":"python developer"
}

dic1 = dic2
print("dic1 is", dic1)
print("dic2 is", dic2)

# now problem in this is if u change anything in dic2 will make changes in dic1 because dic1 is the refernce in dic 2
dic2["company"]  = "Oracle"
print("dic1 is", dic1)
print("dic2 is", dic2)

# so it makes changes in dic1 also

# so to avoid this we use copy() mehtod

dic3 = dic2.copy()
dic2["location"] = "marathalli"
print("dic2 is", dic2)
print("dic3 is", dic3)
print("dic1 is", dic1)

# or dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dic = dict(thisdict)
thisdict['xyz'] = "abc"

print(dic)
print(thisdict)

# setdefault()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.setdefault("color","hmm"))
print(thisdict)



