#1)Print numbers from 1 to 10
'''i=1
while i<=10:
    print(i)
    i+=1

for i in range(1,11):
    print(i)'''

#2)find sum of first 10 natural numbers
'''i=1
while(i<=10):
    n=i*(i+1)/2
    print(n)
    i+=1
    
for i in range(1,11):
    print(i*(i+1)/2)'''

#3)print all even numbers between 1 and 20
'''i=1
while(i<=20):
    if i%2==0:
        print(i)
    i+=1

for i in range(1,21):
    if i%2==0:
        print(i)'''

#4)Program to reverse a given number
'''num=int(input("Enter a value:"))
n=str(num)
print(n[::-1])

num=int(input("Enter a value:"))
a=str(num)
i=0
while i<len(a):
    i+=1
print(a[::-1])'''

#5)check a number is prime
'''num=int(input("Enter :"))
i=2
while (i<=num/2):
    if num%i==0:
        print(num,",Not a prime")
        break
    i+=1
else:
    print(num,",It isprime")
    
    

num=int(input("Enter :"))
for i in range(2,num):
    if num%i==0:
        print(num,",Not a prime")
        break
else:
   print(num,",It is prime")'''

#6)print fibonacci series up to given number 'n'
'''num=int(input("Enter:"))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c)

num=int(input("Enter:"))
a=0
b=1
print(a)
print(b)
i=0
while(i<num):
    c=a+b
    a=b
    b=c
    i+=1
    print(c)
'''


#7)Find factorial of given number
'''n=int(input("Value:"))
i=1
fact=1
while (n>=i):
    fact=fact*i
    i+=1
print(fact)

n=int(input("Value:"))
fact=1
for i in range(fact,n+1):
    fact=fact*i
print(fact)'''


#8)find the sum of digits of a number
'''n=int(input("Enter a value:"))
i=0
sum=0
while(i<=n):
  sum+=i
  i+=1
print(sum)

n=int(input("Enter a value:"))
sum=0
for i in range(n+1):
  sum+=i
print(sum)'''

#9)count the numbers of digits in given number
'''a=[4,56,3478,12,3,45,67]
n=[]
i=0
while i<len(a):
    b=len(str(a[i]))
    n.append(b)
    i+=1
print(n)

a=[4,56,3478,12,3,45,67]
n=[]
for i in range(0,len(a)):
    b=len(str(a[i]))
    n.append(b)
print(n)'''

#10)print all prime numbers between 1 to 100
'''num=int(input("Enter:"))
for i in range(1,num+1):
    if (i<=1):
          pass
    else:
          for j in range(2,i):
              if i%j==0:
                  break
          else:
              print(i,"is a prime")


num=int(input("Enter:"))
i=2
while i<num:
     j=2
     while(j<i):
        if i%j==0:
            break
        j+=1

     else:
          print(i,"is a prime")
     i+=1'''

#11)check a number is armstrong number
'''n=int(input("Value:"))
a=str(n)
l_=len(a)
num=0
for digit in a:
     num+=int(digit)**l_
if num==n:
        print("Armstrong number")
else:
        print("Not a armstrong number")

n=int(input("Value:"))
a=str(n)
l_=len(a)
num=0
i=0
while i<l_:
     num+=int(a[i])**l_
     i+=1
if num==n:
        print("Armstrong number")
else:
        print("Not a armstrong number")'''
       

#12)find the sum of even digits in given number
'''num=int(input("Enter:"))
sum=0
i=0
while i<=num:
    if i%2==0:
        print(i,",",end=' ')
        sum+=i
    i+=1
print("= ",sum,"sum of even numbers")

num=int(input("Enter:"))
sum=0
for i in range(0,num+1):
    if i%2==0:
        print(i,",",end=' ')
        sum+=i
print("= ",sum,"sum of even numbers")'''

    
#13)find the sum of squares of digits in given number
'''num=int(input("Enter:"))
sum=0
for i in range(0,num+1):
    n=i**i
    print(n,",",end=' ')
    sum+=n
print("= ",sum,"sum of square numbers")'''

'''num=2,4,6,9,1,4
sum=0
i=0
while(i<=num):
    n=n[i]**n[i]
    print(n,",",end=' ')
    sum+=n
    i+=1
print("= ",sum,"sum of square numbers")'''


#14)find the Highest common factor(HCF) of two numbers
'''n1=int(input("Number1:")) #max
n2=int(input("Number2:")) #min
if n1< n2: #n1 less than n2, swap it always n1 is greater
    n1,n2=n2,n1
while n2 != 0:
      n1,n2=n2,n1%n2
print("HCF Value:",n1)

n1=int(input("Number1:")) #max
n2=int(input("Number2:")) #min
if n1< n2: #n1 less than n2, swap it always n1 is greater
    n1,n2=n2,n1
for i in range (n2):
      n1,n2=n2,n1%n2
      if n2==0:
        break
print("HCF Value:",n1)'''


#15)guess a number
'''import random
name = input("What is your name:")
print("hey",name,"lets start the game")
computer_guess = random.randint(1,100)
i=1
while(i<=100):
  user_guess = int(input("Guess a number 1 to 100:"))
  print(computer_guess)
  if user_guess == computer_guess:
        print("you win")
  elif user_guess<computer_guess:
        print("guess larger number")
  elif user_guess>computer_guess:
        print("guess lower number")
  else:
       print("guess only numbers in a tuple")
  i+=1

import random
name = input("What is your name:")
print("hey",name,"lets start the game")
computer_guess = random.randint(1,100)
for i in range(1,100):
  user_guess = int(input("Guess a number 1 to 100:"))
  print(computer_guess)
  if user_guess == computer_guess:
        print("you win")
  elif user_guess<computer_guess:
        print("guess larger number")
  elif user_guess>computer_guess:
        print("guess lower number")
  else:
       print("guess only numbers in a tuple")'''

  
#Ranges
#1)Sum of range of numbers
'''n=0
i=0
while(i<=10):
    n+=i
    i+=1
print(n)

n=0  
for i in range(0,11):
  n+=i
print(n)'''

#2)check number is present in a range
'''a=int(input("Number:"))
i=1
while(i<=10):
  if a == i:
     print(a,"present in range")
     break
  i+=1
else:
    print(a,"Not present in range")

a=int(input("Number:"))
for i in range(0,11):
  if a == i:
     print(a,"present in range")
     break
else:
    print(a,"Not present in range")'''


#3)program to range through a dictionary
'''dict_={'a':45,'h':'ghj','56':'goat','d':88}
a_=tuple(dict_.items())
i=0
while i<len(a_):
    print(a_[i])
    i+=1

dict_={'a':45,'h':'ghj','56':'goat','d':88}
a_=tuple(dict_.items())
for i in range(0,len(a_)):
    print(a_[i])'''
   
#4)create set with multiple of set of numbers
'''s_={'a',45,'good',143,'234',True}
s_.add('nithya')
s_.add('sound')   
s_.add('priya')
s_.add('sabari')
s_.add('keerthi')
s_.add('gomu')
s_.add('sumo')
print(s_)'''

       
#5)create a range of numbers
'''i=1
while i<=10:
    print(i)
    i+=1'''

'''for i in range(1,11):
    print(i)'''

            #Enumerate
#1)create a dict with index and fruits
'''str_="apple","mango",'orange',"pomogranate",'papaya'
d_={}
for i,n in enumerate(str_):
  d_[i]=n
print(d_)

#2)create a dict with characters and index
str_="apple"
d_={}
for i,n in enumerate(str_):
    d_[i]=str_[i]
print(d_)'''

#3)create a dict with first char of word and  index which its cube
'''def cube(str_):
  str_="apple","mango",'orange',"pomogranate",'papaya'
d_={}
for i,n in enumerate(str_):
    d_[i]=n
    for i in d_:
        if i **3==i:
            print(i)
print(d_)'''
 
#4)create a list with elements and index and datatype  in tuple(index,datatype)
#5)create a tuple with even index and elements
str_="apple","mango",'orange',"pomogranate",'papaya'
tu_=()
for i in enumerate(str_):
  if len(i[1])%2==0:
    tu_+=(i[1],)
print(tu_)
    
#6)create a list with index and last char elements
#7)create a set with squared index and elements length
#8)create a dictionary with character and index if the index is odd


