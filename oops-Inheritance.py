                                 #-->Inheritance<---


#Single Level Inheritance
'''class Superclass:
    class_name='super class'
    def __init__(self):
        print('In superclass')
    def instance_me(self):
        print(self.class_name)
class Subclass(Superclass):
    def __init__(self):
        print('In subclass')
        super().__init__()
obj1=Subclass()
print(obj1.class_name)
obj1.instance_me()'''

#Multiple Level Inheritance
'''class Baseclass1:
    def __init__(self):
        self.a=10
class Baseclass2:
    def __init__(self):
        self.a=20
class Subclass(Baseclass1,Baseclass2):
    def __init__(self):
        self.a=50
        print(self.a)
        super().__init__()
C1=Subclass()
print(C1.a)'''

#MultiLevel Inheritance
'''class Baseclass1:
    def __init__(self):
        self.a=10
    def display_(self):
        print("Method in Baseclass1")
class Subclass1(Baseclass1):
    def __init__(self):
        self.a=20
        print(self.a)
        #super().__init__()
class Subclass2(Subclass1):
    def display_(self):
        print(self.a)
        
ob1=Subclass2()
print(ob1.a)
#ob1=Subclass1()
#print(ob1.a)'''

#Hierarchical Inheritance
'''class Baseclass:
    def __init__(self):
        self.a=10
        print(self.a)
    def display_(self):
        print('method in baseclass')
class Subclass1(Baseclass):
    def __init__(self):
        print("In subclass")
        super().__init__()
class Subclass2(Baseclass):
    def display_(self):
        print('method in subclass')
        super().display_()
obj1=Subclass1()
obj1.display_()
obj2=Subclass2()
obj2.display_()'''

        

    
