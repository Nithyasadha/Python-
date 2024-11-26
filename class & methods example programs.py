                                  #Class and Methods Example Programs

#1)calculation of percentage,total,average in marks
'''class calculation:
    def __init__(self,stu_name,stu_rn,marks):
        self.student_name=stu_name
        self.student_rn=stu_rn
        self.student_mark=marks
    def student_details(self):
        return (f'''#student_name:{self.student_name}
#student_register_no:{self.student_rn}''')
''' def total_marks(self):
        return sum(self.student_mark)
    def average_mark(self):
        return self.total_marks()/len(self.student_mark)
    def percentage(self):
        return (self.total_marks()/300)*100
student1=calculation('Nithya',64,[85,79,94])
print(student1.student_details())
print("The total marks is",student1.total_marks())
print('Average:',student1.average_mark())
print('Percentage:',student1.percentage())'''

#2)calculation of deposit,withdraw,display in ATM
'''class ATM:
    def __init__(self,per_name,am_,lang_):
        self.person_name=per_name
        self.amount=am_
        self.language=lang_
    def Bank_Account(self):
        return (f'''#person_name:{self.person_name}
#amount:{self.amount}
''')
    def deposit(self,amt_dep):
        self.amount+=amt_dep
        return self.amount
    def withdraw(self,amt_withdraw):
        #if self.amount>=amt_withdraw:
          self.amount-=amt_withdraw
          return self.amount
        #else:
            #print("Invalid balance")
    def display(self):
        return (f'''#person_name:{self.person_name}
#amount:{self.amount}''')
        
'''person1=ATM('Rudhresh',4000,'English')
print(person1.Bank_Account())
print("The person deposited:",person1.deposit(1000))
print("The person withdraw:",person1.withdraw(500))
print("The person total amount:",person1.display())'''

#3)calculation of length and width of area and perimeter
'''class Rectangle:
    def __init__(self,len_,wid_):
        self.length=len_
        self.width=wid_
    def areaperimeter(self):
        return f'''#length:{self.length}
#width:{self.width}'''
''' def area(self):
        return (self.length*self.width)
    def perimeter(self):
        return 2*(self.length+self.width)
value1=Rectangle(5,3)
print(value1.areaperimeter())
print("The Area of rectangle:",value1.area())
print("The Perimeter of rectangle:",value1.perimeter())'''

#4)calculation of some programs in string
'''class String:
    def __init__(self,str_):
        self.string=str_
    def Programs(self):
        return f''' #self.string={self.string}'''
'''def reversestring(self):
        n=input("Enter a string:")
        st_=' '
        i=0
        while(i<len(n)):
           st_=n[i]+st_
           i+=1
        return st_
    def addingstring(self):
        str1=input("Enter:")
        str2=input("Enter:")
        return str1+str2
    def iterablestring(self):
        stri_=input("value:")
        return (','.join(stri_))
    def middlechar(self):
        list_=input("Enter:").split()
        for word in list_:
             w_=(word[-1])            
        return (chr(ord(w_)))
string1=String("Hello world")
print(string1.Programs())
print("Reverse a string:",string1.reversestring())
print("Adding 2  string:",string1.addingstring())
print("Iterable into string:",string1.iterablestring())
print("Middle character:",string1.middlechar())'''

#5)calculate word1 and word2
'''class ClassName:
    def __init__(self,w_1,w_2):
        self.s1=w_1
        self.s2=w_2
    def d_(self):
        return f'''#w1={self.s1}
#w2={self.s2}'''
       
'''def display(self):
        new_str=' '
        for a,b in zip(self.s1,self.s2):
            new_str+=a
            new_str+=b
        return new_str
str1=ClassName('abc','pqr')
print(str1.d_())
print(str1.display())'''

#6)Repeated word return count no of repeatition otherwise false
'''class A:
    def __init__(self,l1):
        self.w1=l1
    def word_(self):
        return f'''#l1={self.w1}'''
''' def display(self):
        l1='ab ab'.split()
        d_=self.w1.split()
        for word in l1:
          if word not in d_:               #wrong
             return False
          else:
             return True
va1=A('abab')
print(va1.word_())
print(va1.display())'''

'''a_=input("Enter:")
d_s=a_*2
m_s=d_s[1:-1]                          #correct without class
if a_ in m_s:
    print(a_.count(a_[:2]))
else:
    print(False)'''

#delete repeated value take unique value(Another method)
'''class C:
    a_=input("Enter:")
    def __init__(self):
        self.a_=None
        self.m_s=None
        self.str_=' ' 
    def repeated_(self,string_):
            self.a_=string_
            self.m_s=(self.a_+self.a_)[1:-1]
            if self.a_ in self.m_s:
                for char in self.a_:
                    if char not in self.str_:
                        self.str_+=char
                print(f'''#{self.str_},is repeated,{self.a_.count(self.a_[:len(str_)])}''')
            '''else:
                print(False)
a1=C()
a1.repeated_('abab')
a2=C()
a1.repeated_('xyxyxy')'''

#7)sort the zero in the end
'''class ob1():
    def __init__(self,value):
        self.v_=value
    def zero(self):
        return sorted(self.v_,key=lambda x:x==0)
c1_=ob1([0,2,0,34,0,45,1])
print(c1_.zero())
c2=ob1([0])
print(c2.zero())'''

#8)



   


        
