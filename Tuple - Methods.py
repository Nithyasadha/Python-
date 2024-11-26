'''t_ = (45,4.5,'hai',(4,5),[2.5,3],45)
print(t_)
print(type(t_))

'single value'
t_1 = (45,)
print(t_,type(t_1))

'constructor'
print(tuple())
print(tuple('Python'),
      tuple([4,5.3,True]),
      tuple({'a','b','c'}),
      tuple({3:45,False:45}))

#Methods in tuple
#count
t_ = (3,4,2.3,'apple',(4))
print(t_.count(4))
print(t_.count('Apple'))

#index
t_ = (3,4,2.4,'apple',(4),3.0)
print(t_.index(2.4))
print(t_.index(3))
print(t_.index(3,1))
print(t_.index('apple'))'''

#tuple is immutable
t_= (3,4,2.3,'apple',(4,),3.0)
t_ [-1] = 4.7
print(t_)

#check indexing and slicing
#1.Program to get even index element
'''tuple2 = ('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[0::2])

#2.Program to get odd index element
tuple2 = ('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[1::2])

#3.Program to reverse the list
tuple2 = ('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[::-1])

#4.Program to get even index element in reverse order
tuple2 = ('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[-1::-2])

#5.[34.5,23,3+6j]
print(tuple2[2::5])

print(tuple2[-3:-6:-1])

#6.[23,3+6j,False,0]z
print(tuple2[3:len(tuple2)])
print(tuple2[:-5:-1])

#operators--> '+','*'
tuple1 = ('Lion','Tiger','Monkey',34,12)
tuple2 = ('Cow','Dog',23,12)
print(tuple1+tuple2)
print(tuple1*2)
'''


