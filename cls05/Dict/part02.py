dicst = {
    'name': 'Tom', 
    'age': 20,
    'brithdate': '1999-01-01'

}

# print(dicst)
#if key in dict

# print('names' in dicst)

#change the brithdate

dicst['brithdate'] = '1999-01-02'
dicst.update({'name': 'Jack'})
print(dicst)


#add item

dicst['birthplace'] = 'beijing'
print(dicst)
