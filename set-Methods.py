#set-->Methods

#1)adding 2 or more set

#add
'''set_ = set()
set_.add('shivam')
set_.add('parvati')
set_.add((3,4))
print(set_)

#union
set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {'a','b','c'}
set_3 = {4.5,3-4j,'kiwi',(9,8)}
print(set_1.union(set_2))
print(set_2.union(set_1,set_3))
print(set_1)

#update
set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {'a','b','c'}
set_3 = {4.5,3-4j,'kiwi',(9,8)}
set_1.update(set_3)
print(set_1)
set_3.update(set_2,set_1)
print(set_3)

#2)Removing the key from the list

#pop
set_1 = {'a',(4,),45,4.4,3-4j,67,'a'}
set_1.pop()
print(set_1.pop())
print(set_1)

#remove
set_1 = {'a',(4,),45,4.4,3-4j,67,'a'}
set_1.remove((4,))
print(set_1)

set_1.remove(23)
print(set_1)'''

#discard
set_1 = {'a',(4,),45,4.4,3-4j,67,'a'}
set_1.discard(67)
print(set_1)

set_1.discard(2.3)
print(set_1)



