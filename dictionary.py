'''
dict_ = {'a':[4,5,6],(True,):{3,4,5},67:4.5,False:True,'a':45}
print(dict_)
print(type(dict_))
print(len(dict_))
print(dict())

#equal to =

print(dict(a=1,b=45,c=23))

#list with list

print(dict[34,'int'],[3.4,[4,5],['a','b'],[34,5]])

#tuple with list

print(dict[(34,'int'),[3.4,[4,5]],['a','b'],[34,5]])

#Method in dictionary
#indexing
dict_ = {'a':[4,5,6],(True,):{3,4,5},67:4.5,False:True,'a':45}
print(dict_['a'])
print(dict_[0])

#get
dict_ = {'a':[4,5,6],(True,):{3,4,5},67:4.5,False:True,'a':45}
print(dict_.get(67))
print(dict_.get(1))
print(dict_.get(1,'no value'))
print(dict_)

#keys
d_ = {'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
print(d_.keys())

#values
d_ = {'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
print(d_.values())

#items
d_ = {'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
print(d_.items())

#Adding key value into a dictionary
#indexing
d_ = {'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_[True] = False
d_[(90,4)] = 'tuple'
print(d_)

#update
d_ = {'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_.update({90:3.4,4+4j:4-3j,'abc':'alpha'})
d_.update([45,45],(3.4,'hai'),'ab',{True,(False,5)})
print(d_)'''

#Removing  key-value pair from a dictionary
#popitem
d_ = {'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_.popitem()
d_.popitem()
print(d_.popitem())
print(d_)

#pop
'''d_ = {'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_.pop(3.4)
d_.pop((4,5,6))
print(d_)

#From keys
string_='string'
print(dict.fromkeys(string_))
print(dict.fromkeys(string_,'str'))

list_=[3,4,5,6]
print(dict.fromkeys(list_,'int'))

tup_ = ('a',)
print(dict.fromkeys(tup_))

set_ = {(90),'kiwi',3.4,56,False}
print(dict.fromkeys(set_,'key'))

#operators in dictionary
'*','|'
#*
d_1 = {3:45,4.4:'float',5:[5,6,7],'6':'a'}
d_2 = {0.4:45,'4.4':'float',5.3:[5,6,7],'69':'a'}
print({*d_1,*d_2})

#|
d_1 = {3:45,4.4:'float',5:[5,6,7],'6':'a'}
d_2 = {0.4:45,'4.4':'float',5.3:[5,6,7],'69':'a'}
print(d_1 | d_2)'''






