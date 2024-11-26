'''#homogeneous
list1 = [23,45,12,895,23,45]
print(list1)

#heterogeneous
list2 = ['23',[43,12,895],34.5,34,3+4j,False,0]
print(list2)

#check length
print("length of else : \n",len(list2)) 

#typecast
print(type(list2)) 

#constructor
#default value
print(list())

#typecasting
#string to list
#according to character
print(list('bangalore is in karn'))

#according to words
print(list('bangalore is in karn'.split()))

#tuple into list
print(list(('bangalore',34,4.5)))

#set into list
print(list({'bangalore',34,4.5}))

#dictionary into list
print(list({'bangalore':45,34:45,4.5:True}))

#indexing
print(list2[0])
print(list2[len(list2)-2])
print(list2[-6],list2[1])
print(list2[1][1],list2[-6][-2])
print(list2[1][2],list2[-6][-1])


print(list2[1][2][1],list2[-6][-1][-2])

#1.Program to get even index element
list2 = ['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[0::2])

#2.Program to get odd index element
list2 = ['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[1::2])

#3.Program to reverse the list
list2 = ['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[::-1])

#4.Program to get even index element in reverse order
list2 = ['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[-1::-2])

#5.Program to get odd index element in reverse order
list2 = ['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[-2::-2])

#6.Program to reverse nested list [45,12,'895']
#7.reverse the string '23'

#8.[34.5,23,3+6j]
print(list2[2:5:])
print(list2[2::5])
print(list2[-3:-6:-1])

#9.[23,3+6j,False,0]
print(list2[3:len(list2)])
print(list2[:-5:-1])

#10.[23,False]
print(list2[3::2])
#reverse
print(list2[-2:-5:-2])'''

#indexing
li2 = [45,3.5,2.3,'Hey',[True,False]]
li2[-2] = 'hey'
print(li2)

#slicing
li2 = [45,3.5,2.3,'Hey',[True,False]]
li2[0:2] = [34,67]
print(li2)
li2[-2::] = ['apple']
print(li2)
li2[2:4] = 'apple'
print(li2)


















