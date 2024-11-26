#1)Write a python program to check whether the given number is even or odd
   #normal way
'''i=int(input("Enter:"))
if i%2==0:
    print(True)
else:
        print(False)'''

   #userfedined function
'''def even_num(i=int(input("Enter:"))):
 if i%2==0:
    return True
 else:
    return False
print(even_num())'''

  #Anonymous function
'''n=int(input("Enter:"))
even_num=lambda n:n%2==0
print(even_num(n))'''

#2)WAPP odd numbers inbetween range
  #user defined function
'''def oddnum(l):
    for i in l:
        if i%2!=0:
            print(i)
oddnum([1,3,4,10,7,8])'''

  #anonymous function
    #@to get single data
'''oddnum=lambda num:num%2!=1
print(oddnum(2))
print(oddnum(17))'''
     #@to get multiple data
'''oddnum=lambda n:n%2!=1
print(tuple(filter(oddnum,[1,3,4,10,7,8])))'''

  #anonymous function with user defined function
'''def oddnum(l):
    if l%2==1:
        return l
print(list(filter(oddnum,[1,3,4,7,10])))'''

#3)WAPP to get sum of the even numbers in the range
  #without sum function
'''def sum_even(startn,endn):
    sum_=0
    for n in range(startn,endn+1):
        if n%2==0:
            sum_=sum_+n
    print(sum_)'''

     #with sum function
'''def sum_even(startn,endn):
    l_=[]
    for n in range(startn,endn+1):
        if n%2==0:
            l_.append(n)
    print(l_)
sum_even(1,10)'''

  #comprehension
'''def sum_even(s,e):
    print(sum([n for n in range(s,e+1) if n%2==0]))
sum_even(20,30)'''

#4)WAPP to check whether the given number is special numbers or not
'''def spe_num(num):
    sum_=sum([int(i) for i in str(num)])
    p=1
    for i in str(num):
        p*=int(i)
    if sum_+p==num:
            return"Special number"
    else:
            return "Not a special number"
print(spe_num(29))'''

'''n=int(input("Enter:"))
a=str(n)
k=0
m=1
for digit in a:
    k+=int(digit)
    m*=int(digit)
j=m+k
if j==n:
    print("Special number")
else:
    print("Not a special number")'''

#5)WAPP to print multiplication table to the given number in a range
'''n=int(input("Enter:"))
for i in range(1,10+1):     #for single table
    print(n,'*',i,'=',n*i)'''


for i in range(1,5+1):
    for j in range(1,10+1):    #to get range tables
        print(i,'*',j,'=',i*j)

'''s_=int(input("Enter1:"))
e_=int(input("Enter2:"))
for i in range(s_,e_+1):
    for j in range(1,10+1):    #to get range tables
        print(i,'*',j,'=',i*j)'''

#6)WAPP check whether the number is neon number
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

#7)WAPP to find the factors of a given number
'''n=int(input("Enter:"))
for i in range(1,10+1):     
    print(n,'*',i,'=',n*i)'''

'''def factors_(i=1,num=int(input("Enter anumber:"))):
    if i<=num:
        if num%i==0:
             print(i,end=' ')
        return factors_(i+1,num)
factors_()'''

#8)WAPP to check the number is xylem and phloem
'''num=int(input("Enter:"))
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

#9)WAPP GCD between two numbers
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

#10)WAPP to check whether the given number is strong number or not
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


#1)
'''n=int(input("Enter the number:"))
s_=set()
for i in range(1,n+1):
    s_.add(i)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
l_=list(s_)
print(gcd(l_[0],l_[-1])+gcd(l_[1],l_[2]))'''

#2)Write a program to get nth fibonacci number
'''n=int(input("Enter:"))
a=0
b=1
i=0
while i<n-1:
        c=a+b
        a=b
        b=c
        i+=1
print(c)'''

'''def print_(i=0,a=0,b=1):
    if i<n-1:
        c=a+b
        a=b                                #error
        b=c
        return print_(i+1,c)
    else:
        return c
print(print_())
'''
'''def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n=6
print(f"{n}th fib is {fib(n)}")'''


#2)Write a program to create a recursion function for power of a number
'''n=int(input("Enter1:"))
m=int(input("Enter2:"))
pow=n**m                                  #(normal way)
print(pow)'''

'''def pow_(n,m):                      #error
    pow=n**m
print(pow_())'''


'''def power(base,exp):
    if exp<=0:   #if exp==0:
        return 1
    return base*power(base,exp-1)
print(power(2,4))'''


#3)write a program to count number of digits in recursion function
'''n=int(input("Enter:"))
for i in range(n):
  m=len(str(i))
print(i)'''                      #error

'''def print_(n):
    if n<10:
        return (n)
    else:
        return count(n)'''
#4)write a recursion function to get the triangular number
'''def triangular_num(n):
    if n<=1:
        return 1
    return n+triangular_num(n-1)
print(triangular_num(5))
print(triangular_num(10))'''










    





        


