#Activity-->Tuple
#1)
tu_ = (21,67,'hello',(6,2,1),[2.3],'goat')
print(tu_,type(tu_))

#2)
t1 = (1,2,3)
t2 = (4,5,6)
print(*t1,*t2)

#3)
t= (1,2,3,4,['hai','hello',123],'python')
t1=str(t)
print(t1.replace('y','Y'))

t= (1,2,3,4,['hai','hello',123],'python')
t1=str(t)
print(t1.replace('2,3,4','9,10,11'))

#4)
tuple1 = (4,8,2,7.2,'apple',(3,),9)
t2=list(tuple1)
t2.append('mango')
print(t2)
t3=tuple(t2)
print(t3)

#5)
tuple1 = (4,8,2,7.2,'apple',(3,),9)
tu_=list(tuple1)
tu_.remove(8)
tu_.remove(2)
print(tu_)'''


