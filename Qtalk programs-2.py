#1)Program to check a number is prime or not
'''number = int(input("Enter a number: "))
for n in range(2,number):
    if number%n == 0:
        print("It is not a prime number")
        break
else:
    print("It is a prime number")
    
#2)Program to get prime number in a range
s_v = int(input("Enter a number: "))
e_v = int(input("Enter a number: "))
for i in range(s_v,e_v+1):
    for j in range(2,i):
       if i%j == 0:
          break
    else:
        print(i,end=' ')

s_v = int(input("Enter a number: "))
e_v = int(input("Enter a number: "))
for i in range(s_v,e_v+1):
    if i<=1:
        pass
    else:
       for j in range(2,i):
           if i%j == 0:
              break
       else:
        print(i,end=' ')'''

#3)Program to get a factorial
num_= int(input("Enter a number:"))
fact_=1
for i in range(fact_,num_+1):
    fact_=fact_*i
print("factorial of ",num_,"is",fact_)

#4)Program to print fibonnacci number
'''num_=int(input("Enter a number:"))
a=0
b=1
print(a)
print(b)
for i in range(2,num_):#(2,5)=2,3,4=2|3|4
    c=a+b #0+1=1|1+1=2|1+2=3
    a=b #a=1|
    b=c #b=1|
    print(c)

num_=int(input("Enter a number:"))
a=0
b=1
if num_<=1:
    print(0)
else:
   print(a)
   print(b)
   for i in range(2,num_):#(2,5)=2,3,4=2|3|4
        c=a+b #0+1=1|1+1=2|1+2=3
        a=b #a=1|
        b=c #b=1|
        print(c)
    '''
#5)Program to  check armstrong number
num_=int(input("Enter a number:"))
a=len(str(num_))
n=0
for digit in str(num_):
    n+=int(digit)**a
if num_==n:
    print("Armstrong number")
else:
    print("Not a armstrong number")
'''for i in range(num_):
    print(i*b)'''
  

