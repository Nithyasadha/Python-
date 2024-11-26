#In numbers

#1)WAPP to print Multiplication Table To the Given Number?
'''n=int(input("Enter:"))
for i in range(1,10+1):     #for single table
    print(n,'*',i,'=',n*i)'''

#2)WAPP to print Multiplication Tables Between the Range?
'''for i in range(1,5+1):
    for j in range(1,10+1):    #to get range tables
        print(i,'*',j,'=',i*j)'''

'''s_=int(input("Enter1:"))
e_=int(input("Enter2:"))
for i in range(s_,e_+1):
    for j in range(1,10+1):    #to get range tables
        print(i,'*',j,'=',i*j)'''

#3)WAPP to check whether the given number is neon number or not..?
'''num=int(input("Enter a number:"))
m_=0
n=num**2
for digit in str(n):
    m_+=int(digit)
if m_==num:
        print("It is neon number")
else:
        print("Its is not a neon number")'''

'''def neon(num=int(input("Enter a number:"))):
    m_=0
    n=num**2
    for digit in str(n):
        m_+=int(digit)
    if m_==num:
        print("It is neon number")
    else:
        print("Its is not a neon number")
neon()'''

#4)WAPP To Find The factors to the Given Number?
'''XYlem and phloem
num=int(input("Enter:"))
m_=0
if len(str(num))>2:
    n=int(str(num)[0])+int(str(num)[-1])
for digit in str(num)[1:-1]:
           m_+=int(digit)
if n>m_:
           print("It is Xylem")
elif n<m_:
            print("It is Phloem")
else:
    print("It is equal number")'''

#5)WAPP To Find The factors to the Given Number?
'''n=int(input("Enter:"))
for i in range(1,10+1):     
    print(n,'*',i,'=',n*i)'''

'''def factors_(i=1,num=int(input("Enter anumber:"))):
    if i<=num:
        if num%i==0:
             print(i,end=' ')
        return factors_(i+1,num)
factors_()'''

#6)WAPP to Print GCD in between two Number?
'''def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(25,5))'''

'''n=int(input("value1:"))
m=int(input("value2:"))
if (m==0):
    print(n)
else:
    print(m,n%m)'''

#7)WAPP to check whether the Given Number is Strong Number or Not? 
'''num=int(input("Enter:"))
sum_=0
for digit in str(num):
    n=int(digit)
    fact_=1
    for i in range(fact_,n+1):
        fact_=fact_*i
    sum_+=fact_
if sum_==num:
    print("Strong number")
else:
    print("Not a strong number")'''

'''def strong(num=int(input("Enter:"))):
    sum_=0
    for digit in str(num):
        n=int(digit)
        fact_=1
        for i in range(fact_,n+1):
            fact_=fact_*i
        sum_+=fact_
    if sum_==num:
        print("Strong number")
    else:
        print("Not a strong number")
strong()'''

#8)WAPP To Check Whether The Given Number Is Even or Not?

#9)WAPP To Print Odd Numbers In Between The Range?

#10)WAPP to Get Sum The Even Numbers In BetWeen The range?

#11)WAPP To Count the Digits Present In The Given Number?

#12)WAPP To Get Sum Of The Digits Present in the Given Number?

#13)WAPP To Get Product Of the Digits Present in the given number?

#14) WAPP To Check Whether The Given Numbers SPY number or not? 

#15)WAPP to Check WhetherThe Given Number Is Buzz Number or Not?

#16)WAPP to Print Largest Digit Present in the given number?

#17)WAPP to print Smallest Digit Present in the Given Number?

#18)WAPP To Check Whether the given number is perfect number or not?

#19)WAPP to Check Whether the given number prime number or not?

#20)WAPP to get Sum of the prime Numbers Between The Range?

#21)WAPP to Find The Factorial of the Given Number?

#22)WAPP To get sum of the factors to the given number?

#23)WAPP to find the power in between N and P?

#24)WAPP to Check Whether The given Number is ArmStrong Number or Not?

#25)WAPP to print Square Root Of the Given Number? 

#26)WAPP to Check Whether The Given Numberis Sunny Number or Not…?

#27)WAPP to check whether the Given Number First Digit is Even Or Odd..?

#28)WAPP to Check WhetherThe Given Number Is AutoMorphic Number Or Not…?

#29)WAPP to Check whether The Given Number Is TechNumber Or Not..?

#30)WAPP to check Whether The Given Number is Happy Number Or Not?
