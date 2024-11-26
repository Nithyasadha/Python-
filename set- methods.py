#To get common key in set
#1)Intersection 
'''set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {('a','b','c'),4.4}
set_3 = {4.5,3+4j,'kiwi',(9.8),'a'}
print(set_1.intersection(set_2))
print(set_1.intersection(set_3))
print(set_2.intersection(set_1,set_3))

#2)Intersection update
set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {('a','b','c'),4.4}
set_3 = {4.5,3+4j,'kiwi',(9.8),'a'}
set_2.intersection_update(set_1)
print(set_2)
set_1.intersection_update(set_2,set_3)
print(set_1)

#To get uncommon keys in set
#1)Difference
set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {('a','b','c'),4.4}
set_3 = {4.5,3+4j,'kiwi',(9.8),'a'}
print(set_2.difference(set_2))
print(set_3.difference(set_2,set_1))

#2)Difference_update
set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {('a','b','c'),4.4}
set_3 = {4.5,3+4j,'kiwi',(9.8),'a'}
set_3.difference_update(set_1,set_2)
print(set_3)

#3)symmetric difference
set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {('a','b','c'),4.4}
set_3 = {4.5,3+4j,'kiwi',(9.8),'a'}
print(set_2.symmetric_difference(set_1))
print(set_1.symmetric_difference(set_3))
print(set_2.symmetric_difference(set_2))

#4)
set_1 = {'a',(4,),45,4.4,3-4j,False,'a'}
set_2 = {('a','b','c'),4.4}
set_3 = {4.5,3+4j,'kiwi',(9.8),'a'}
set_3.symmetric_difference_update(set_1)
print(set_3)
set_1.symmetric_difference_update(set_2)
print(set_1)

#
#1)issubset
s1={3,'a','%&',9.8}
s2={3,'a',3+4j,'%&',9.8,(45),56.4}
print(s1.issubset(s2))
s1={3,'a','%&',9.8}
s2={3,'a',3+4j,'%&',(47),56.4}
print(s1.issubset(s2))

#2)issuperset
s1={3,'a','%&',9.8}
s2={3,'a',3+4j,'%&',9.8,(45),56.4}
print(s1.issuperset(s2))
print(s2.issuperset(s1))

#3)isdisjoint
s1={34,90,23}
s2={3,4,5,17,9}
s3={34,56,12,45}
print(s1.isdisjoint(s3))
print(s2.isdisjoint(s3))

#operators
#'-'-->difference
print({3,4,3}-{4,'R',55,6})
s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_-s_1)

#'^'-->symmetric difference
s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_^s_1)'''

#'&'-->intersection
s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_&s_1)

#'|'-->union
s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_|s_1)

