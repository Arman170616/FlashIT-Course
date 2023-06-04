#loop through the dictionary and print the key and value

dicst = {
    'name': 'Tom',
    'age': 20,
    'brithdate': '1999-01-01',
    'birthplace': 'beijing'
  }   

#keys()
# for x in dicst.keys():
    # print(x)

#values()
# for x in dicst.values():
    # print(x)

#items()
# for x in dicst:
#     print(x, dicst[x])


# for x,y in dicst.items():
#     print(x, y)


#copy()

dicst2 = dicst.copy()
print(dicst2)

mydict = dict(dicst)
print(mydict)
