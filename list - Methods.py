'''
1) Insert element from the list

# list-->Append Method

list1 = [34.5,"arun",43,{1,2,3,4},[True,False]]
list1.append(3+4j)
list1.append('kalps')
print(list1)

#list-->Extend Method

list1 = [34.5,"arun",43,{1,2,3,4},[True,False]]
list1.extend('hai')
list1.extend(['hai',45,False,7.8])
print(list1)

#list-->Insert Method
list1 = [34.5,"arun",43,{1,2,3,4},[True,False]]
list1.insert(0,'bangalore')
list1.insert(4,45)
print(list1)

#2.removing  element  from the list

#list--> pop method

l1 = [56,31,78,21,89]
l1.pop()
l1.pop(2)
print(l1)

#list--> remove Method

l2 = [56,31,78,21,89,89,56]
l2.remove(31)
l2.remove(56)
print(l2)'''

'''#list--> del Method

l3 = [56,31,78,21,89,89,56]

#indexing:
del l3[4]
del l3[-1]
print(l3)

#slicing:
l3 = [56,31,78,21,89,89,56]
del l3[:2]
print(l3)

del l3[2:5]
print (l3)

del l3[::2]
print(l3)

del l3[1::2]
print(l3)'''


'''# Methods in a list

#reverse
l3 = ['a',45,4.5,[4,3],True]
print(l3[::-1])
l3.reverse()
print(l3)

#Index
l3 = ['a',45,0,4.5,[4,3],True,1,False]
print(l3.index(False))
print(l3.index(False,3))
print(l3.index('a'))
print(l3.index(1))'''

'''#count
l3 = ['a',45,0,4.5,[4,3],True,1,False,True]
print(l3.count('a'))
print(l3.count(True))
print(l3.count([3,4])) 

#sort
list_ = [3,4,12,78,4.5,78,0,1]
list_.sort()
print(list_)
list_.sort(reverse=False)
print(list_)
list_.sort(reverse=True)
print(list_)

li_ = ['apple',"Apple",'grapes','Van','Wayanad','TN',"avacoda"]
li_.sort()
print(li_)

l_ = ["3+4j","1+4j","3+5j"]
l_.sort()
print(l_)

l_1 = [True,False]
l_1.sort()
print(l_1)

#copying the list
#normal copy
li_= ["Apple","apple",["grapes","van","wayanad"],"TN","avacado"]
li_2= li_
print(li_)
print(li_2)
print(id(li_),id(li_2))
print(id(li_[2]),id(li_2[2]))'''

#shallow copy
li_= ["Apple","apple",["grapes","van","wayanad"],"TN","avacado"]
li_2= li_.copy()
print(li_)
print(li_2)
print(id(li_),id(li_2))
print(id(li_[2],id(li_2[2])))

#deep copy
from copy import deepcopy
li_ = ["Apple","apple",["grapes","van","wayanad"],"TN","avacado"]
li_2 = deepcopy(list1)
print(li_)
print(li_2)
print(id(li_),id(li_2))
print(id(li_[2],id(li_2[2])))


'''#Operators in list
list1 = ['apple',"hello","orange","hai"]
list2 = ['keerthi',"priya","sound","sabari","raji"]
print(list1+list2)
print(list1*3)

#ord and chr
print(ord('t'), ord('1'), ord('&'))
print(chr(65),chr(100),chr(32),chr(2))'''



        










