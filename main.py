'''
round brackets
it is ordered
immutable
Elements do not have to be unique
different data types- intergers, strings 
'''
'''
Creating Tupe
'''
tuple = ()
tuple = ('cat', [4,3,2,1], (1,2,3))
tuple = 1234, 4321
#pyhon sees it as tuple
tuple = 'hello',
tuple = ('hello',)
#coma at the end make the string a tuple
print(tuple)

'''
Access Tuple
'''
tuple2 = (1234, 4321, 'hello')
print(tuple2[-1])

'''
Slicing tuple
'''
fruits = ('orange', 'apple', 'pear', 'grapes','banana')
print (fruits[:])
# print (fruits[2:5])
#print between 2 and 5 index
print (fruits[:-2])
#removes last two items
print (fruits[:2])
#prints from 0 to 2

# print (fruits[::2])
#skip every other 2

print (fruits[::-2])
#prints in reverse order skipping 2

'''
Changing tuple
'''
# fruits2 = ('orange', 'apple', 'pear', 'grapes','banana')
# fruits2[3] = 'maize'
#cannot mutate tuple. that is why they are fast


'''
deleting a tuple
'''
fruits3 = ('orange', 'apple', 'pear', 'grapes','banana')
# del fruits3[0]
#you cannot delete an item
# del fruits3
# print(fruits3)
#it will dete the tuple as a whole


'''
Tuple Method
'''
print(dir(tuple))
#only index and count are the built in methods
fruits = ('orange', 'apple', 'pear', 'grapes','banana')
print(fruits.count('orange'))
print(fruits.index('apple'))



'''
Slicing tuple
'''