# list 
#ordered
#changeable
#allow duplicates

list1 = [1, 2, 3, 4, 5, 2]
# print(type(a))
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)

# print(a[3])

#cheack if item exists

# if 2 in list1:
#     print('yes')

#change item value

# list1[2] = 10

# print(list1)

#insert item

# list1.insert(0, 9)
# print(list1)


#append item

list1.append(10)
# print(list1)

#remove item
# list1.remove(10) #remove by 10
# print(list1)

list2 = [1, 2, 3, 4, 5, 2]

# list1.extend(list2)
# print(list1)

# list1.pop(2) #remove by index
# print(list1)

#delete list
# del list1
# print(list1)

# list1.clear()
# print(list1)


#loop through list
# for x in list1:
#     print(x)


#list comprehension

# [print(x) for x in list1]



a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [x for x in a if x < 5]
print(a)

#join two list

list3 = list1 + list2
print(list3)