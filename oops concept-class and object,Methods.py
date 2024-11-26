


                                #1.Class Variable

'''
class MarutiSuzuki:
    car_name='swift'
    color='white'
    fuel='petrol'
    gear='manual'
car1=MarutiSuzuki()
car2=MarutiSuzuki()
                                   #'Accessing'
#class_name
print(MarutiSuzuki.car_name)
print(MarutiSuzuki.gear)

#object_name
print(car1.color)
print(car2.fuel)



                                  #'Modifying'
#class_name
print(MarutiSuzuki.color)
MarutiSuzuki.color='red'
print(MarutiSuzuki.color)
print(car1.color,car2.color)

#object_name
print(car1.gear)
car1.gear='auto'
print(car1.gear)
'''
                                  #2.Instance Variable
'''class College:
    college_name='sona college'
    def __init__(self):
        self.stu_name='Nithya'
        self.reg_no=64
        self.branch='AI'
        self.age=20
        print(self.stu_name, self.reg_no,self.branch, self.age)
        
student1=College()
print(College.college_name)
print(student1.college_name)
print(student1.branch)'''

'''class College:
    college_name='sona college'
    def __init__(self,name,rn,brn,age):
        self.stu_name=name
        self.reg_no=rn
        self.branch=brn
        self.age=age
        print(self.stu_name, self.reg_no,self.branch, self.age)
        
stu1=College("Ashwin",65,'CS','29')
stu2=College("Ramesh",69,'Biotech','34')'''


                                               #2.Methods
#i)Instance Method
'''class IPhone:
    phone_name='15pro'
    def __init__(self,storage,camera,ram,color):
        self.storage=storage
        self.camera=camera
        self.ram=ram
        self.color=color
    def phone_details(self):
        print(f'''''''storage:{self.storage}
                   camera:{self.camera}
                   ram:{self.ram}
                   color:{self.color}''''''
phone1=IPhone(256,'12px',6,'blue')
phone1.phone_details()
IPhone.phone_details(phone1)'''

#ii)Class Method
'''class IPhone:
    phone_name='15pro'
    def __init__(self,storage,camera,ram,color):
        self.storage=storage
        self.camera=camera
        self.ram=ram
        self.color=color
    @classmethod
    def details2(cls):
         print(cls.phone_name)
         cls.phone_name='redmi'
         print(cls.phone_name)
phone1=IPhone(256,'12px',16,'blue')
IPhone.details2()
phone1.details2()
               '''

#iii)Static Method
'''class IPhone:
    phone_name='15pro'
    def __init__(self,storage,camera,ram,color):
        self.storage=storage
        self.camera=camera
        self.ram=ram
        self.color=color
    @staticmethod
    def details3():
        print('static method is independent of self and cls')
        #print([for i in range(1,11)])
phone1=IPhone(256,'12px',16,'blue')
phone1.details3()
IPhone.details3()'''


    



    
    



    
    
   
