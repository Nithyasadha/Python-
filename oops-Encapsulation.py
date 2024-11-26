                      #-->Encapsulation<---
#Access Specifier
'''class Atm:
    bank=input("Bank_name?")
    def __init__(self,lan_,balance,pin):
        self.language=lan_
        self._amount=balance
        self.__password=pin
    def object_method(self):
        print(''' 
#language:{self.language}                  #pin execute error because it is private access specifier
#amount:{self.amount}
#pin:{self.pin}''')
'''def class_method(cls):
       print(cls.bank)
user1=Atm("Telegu",500,1234)
print(user1.language)
print(user1._amount)
print(user1.__pin)'''





#Property Decorator
'''class Student:
    def __init__(self):
        self.__mark=35
    @property
    def method(self):
        pass
    @method.getter
    def method(self):
        return self.__mark
    @method.setter
    def method(self,new_value):
        self.__mark=new_value
    @method.deleter
    def method(self):
        del self.__mark
        print("Value deleted")
stu1=Student()
print("Initial value:",stu1.method)
stu1.method=40
print("modified value:",stu1.method)
del stu1.method'''

              
#1)Find area of width and height of rectangle
'''class Rectangle:
    def __init__(self,width,height):
       self.__width=width
       self.__height=height
    @property
    def area(self):
        return self.__width*self.__height
    @property
    def length(self):
        return self.__height
    @length.setter
    def length(self,value):
        self.__height=value
    @property
    def breadth(self):
        return self.__width
    @breadth.setter
    def breadth(self,value):
        self.__width=value
area1=Rectangle(10,20)
print('length:',area1.length,'width:',area1.breadth)
print("area of initial values:",area1.area)
area1.length=20
area1.breadth=34
print('length:',area1.length,'width:',area1.breadth)
print("area of modified values:",area1.area)'''


#2)Find radius,diametre,circumference of area of circle
class Circle:
    def __init__(self,radius):
        self.__radius=radius
        self.pi=3.14
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,value):
         self.__radius=value
    @property
    def diameter(self):
        return 2*self.__radius
    def circumference(self):
        return 2*self.pi*self.__radius
radius1=Circle(10)
print('radius of circle',radius1.radius)
print("diameter of the circle",radius1.diameter)
print("Circumference of the circle",radius1.circumference)
radius1.radius=20
print('modified radius of circle',radius1.radius)
print("modified radius of circle:",radius1.radius)
print("modified diameter of the circle",radius1.diameter)
print("modified Circumference of the circle",radius1.circumference)




    
