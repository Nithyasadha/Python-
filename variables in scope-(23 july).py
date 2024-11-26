#variable in scope
                        #global variable
'''a=10
def f1():
    print(a,"inside a function")
f1()
print(a,"outside a function")

                        #Local variable
a=10
def f1():
    a=20
    print(a,"inside a function")
f1()
print(a,"outside a function")

#convert local to global variable
a=10
def f1():
    global a
    a=20
    print(a,"inside a function")
f1()
print(a,"outside a function")

#1)convert local to global variable(use global keyword to convert into global variable)
a=10
def f1():
    global a
    a=20
    print(a,"inside a function")
f1()
print(a,"outside a function")

#2)convert local to global variable
         #return keyword
#eg:1
a=10
def f1():
    a=10
    return a
a1=f1()
print(a1)

#eg:2
def f1():
    return
a1=f1()
print(a1)

#eg:3
def f1(a,b):
    return a+b,a*b
a1=f1(10,20)
print(a1)

#3)Non local variable
def f1():
    num=100
    def f2():
        num=200
        print(num)
    f2()
    print(num)
f1()'''

#1)convert local to global(use nonlocal keyword to convert into global variable)
def f1():
    num=100
    def f2():
        nonlocal numss
        num=200
        print(num)
    f2()
    print(num)
f1()
