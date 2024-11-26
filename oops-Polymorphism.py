                  #-->Polymorphism<--


#1)Polymorphism with respect to function
'''print(len('Polymorphism'))
print(len([3,4.5,'hai']))
print(len({3,4.4,5,'hai'}))
print(len({2:3,4:5,3:1,2.5:1}))'''
#2)Polymorphism with respect to operators
'''
'+'
print(5+6,'5'+'6')
'*'
print(4+5,*[3,1,6],'hai'*3)
'-'
print({24-10,54,5,1}-{3,1,4})
'&'
a=10
b=20
print({4,5,1}&{3,1,4},a&b)
'|'
print(a|b)
print({4:5}|{3:4})'''

#3)Polymorphism with respect to method
'''class A:
    def display(self):
        print("Hi")
class B:
    def display(self):
        print("Hello")
#0ne way
a1=A()
a1.display()
a2=B()
a2.display()

#second way
for method in (a1,a2):
    method.display()'''

#4)Polymorphism with respect to inheritance
'''class A:
    def display1(self):
        print("In method A")
class B(A):
    def display1(self):
        print("In method B")
b=B()
b.display1()'''

'super'
'''class A:
    def display1(self):
        print("In method A")
class B(A):
    def display1(self):
        print("In method B")
        super().display1()
b=B()
b.display1()'''


