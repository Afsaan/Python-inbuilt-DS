"""
Write a Python script to sort (ascending and descending) a dictionary by value.
"""
import operator
y=[]
for i in range(4): # to take dictionary as per as user choice
    keys = input("enter keys : - ")
    values = input("enter the value for "+keys +":-")
    x = (keys,values)
    y.append(x)

ascen = sorted(y,key=operator.itemgetter(1))
dic = dict(ascen)
print(dic) # in ascending order

desc = sorted(y,key=operator.itemgetter(1),reverse=True)
dic = dict(desc)
print(dic)






