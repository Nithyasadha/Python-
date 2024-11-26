#Activity 2--> List
#1)
Name1 = ['apple','google','amazon','facebook','instagram','microsoft']
Name1.append(['netflix','prime','hotstar'])
print(Name1)

#1)
Name1 = ['apple','google','amazon','facebook','instagram','microsoft']
Name1.extend('prime')
Name1.extend(['netflix','prime','hotstar'])
print(Name1)

#2)
li_ = [23,45,'pop','Example','list']
li_.pop()
print(li_)
li_.pop(2)
print(li_)

#2)
li_ = [23,45,'pop','Example','list','pop',45]
li_.remove(23)
print(li_)
li_.remove('pop')
print(li_)

#3)
list5 = [23,45,0,4,10,67,105,43,458]
list5.sort()
print(list5)
list5.sort(reverse=False)
print(list5)
list5.sort(reverse=True)
print(list5)

#4)
string = "Developers in Pyspider"
print(list(string))
print(string.split( ))

