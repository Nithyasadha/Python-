#1)Positional argument
'''eg:1def f1(name,age,id):
    return name,age,id
print(f1("nithya",20,64))

eg:2
def f2():
    c=10
    return c
print(f2())'''

#2)Keyword argument
'''eg:1
def func(name,age):
    print(name,age)
func(age=23,name="Neha")'''

'''eg:2
def func(name,age):
    print(name,age)
func(23,"Neha")'''

#3)combination of positional and keyword argument
'''eg:1
def func(name,age):
    print(name,age)
func("Rani",age=46)

eg:2
def f1(name,age,id):
    return f"name:{name}\n age:{age}\n id: {id}"
print(f1('rani',34,3))'''

#4)Only positional and keyword argument
#i)Only positional argument
'''eg:1
def func(name,age,/,id):
    print(name,age)
func("Rani",45,2)
func("Riya",30,id=4)

eg:2
def f1(a,b,/,c,d):
    print(a,b,c,d)
f1(10,20,45,45)
f1(10,20,c=45,d=45)
f1(10,20,45,d=45)'''
#exception-->before'/' don't give variable name it shows exception
#f1(a=10,b=20,45,d=45)

#ii)Only keyword argument
'''eg:1
def func(name,age,*,id):
    print(name,age)
func("Rani",42,id=4)
func(name="A",age=25,id=4)

eg:2

def f1(a,b,*,c,d):
    print(a,b,c,d)
f1(a=10,b=34,c=45,d=45)
f1(10,34,c=45,d=45)
f1(10,b=34,c=45,d=45)'''

#5)variable positional arguments
'''def func(*args):
    print(args)
func(3,4,5)
func('hai',[4,5,6],True)'''

#6)variable keyword argument
'''ex:1
def fun(**kwargs):
    print(kwargs)
fun(a=34,b=3.6,c=False,d='python',e=[False,True])

ex:2

def fun(string_,*args,**kwargs):
    print("\n",string_,"\n",args,"\n",kwargs)
fun(3.4,list=3.6,False,d='python',c=[False,True])'''

#7)default argument
'''ex:1
def fun(a,b):
    return a**2,b**3

print(fun(3,5))

ex:2
def fun(a=2,b=10):
    return a**2,b**3

print(fun(3,5))
print(fun(4))
print(fun())'''

#Programs
#1)A function takes variable number of positional arguments as input. 






#2)write a function to print below output
#func("TRACXN",0) #RCN
#func("TRACXN",1) #TAX
def f1(str_,n):
    if (n==0):
        print(str_[1::2])
    elif n==1:
        print(str_[::2])
f1("TRACXN",0)
f1("TRACXN",1)



