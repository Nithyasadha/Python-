                                        #RANGE

#1)Program tp print number from 1 to 10

#using while loop
'''i =1
while i<11:
    print(i)
    i+=1
#range (type caste)
r1=range (1,11)
print(list(r1))

#using for loop
for n in r1:
    print(n,end=' ')

#2)Program to print the numbers from 10 to 1
for n in range(10,0,-1):
    print(n,end=' ')

#3)Program to print the numbers from -10 to -1
for n in range(-10,0):
   print(n,end=' ')

#4)Program to print the numbers from -10 to 5
for n in range(-10,6,1):
    print(n,end=' ')

#5)program to print the numbers from 20 to -15
for n in range(20,-16,-1):
    print (n,end=' ')

#6)program to print the numbers from -20 to -15
for n in range(-20,-14,1):
    print (n,end=' ')

#7)program to get only even number from user input
n= int(input("Enter a start value:"))
m= int(input("Enter a start value:"))
for i in range (n,m):
  if i%2==0:
      print(i,"even number")

#8)program to get only odd number from user input
a= int(input("Enter a start value:"))
b= int(input("Enter a start value:"))
for i in range (a,b):
  if i%2!=0:
      print(i,"odd number")

                                  #ENUMERATE
                                  
#1)program to get the word and index using for loop
#(for loop and index)
str_=input("Enter a string:").split()
for n in range(len(str_)):
    print(n,str_[n])

str_=input("Enter a string:").split()
t_=()
for n in range(len(str_)):
    t_+=(n,str_[n])
print(t_)

#Typecast
str_=input("Enter a words:").split()
#print(tuple(enumerate(str_)))
print(enumerate(str_))

#for loop
`str_=input("Enter a words:").split()
for t in enumerate(str_,1):
    print(t)

#2)Create a tuple with index and length of each words
str1 = "hello guys see on the screen and do this program"
tu=()
for n,word in enumerate(str1.split()):
    tu+=((n,len(word)),)
print(tu)

#3)Create a set with index and word with even length only
str1 = "sharing is caring as always"       #doubt
for n,word in enumerate(str1.split()):
  print({(n,str1[n]),word[::2]})

str1 = "sharing is caring as always"
s_=set()
for i,word in enumerate(str1.split()):
    if len(word)%2==0:
        s_.add(word)
print(s_)

#4)Create a dictionary with square of index and 1st char of word
str2 = "Old is gold"
d_={}
for i,word in enumerate (str2.split()):
    d_.update({word[0]:str2.index(word[0])})
print(d_)'''

                                                                #ZIP






#1)Program to add the numbers in same indexes
'''lis1=input("Enter a value:").split()
lis2=input("Enter  a value:").split()
from itertools import zip_longest
for i,j in zip_longest(lis1,lis2,fillvalue=10):
    print(f'{int(i)}+{int(j)}={int(i)+int(j)}')'''

#2)Program to square the numbers in 1st and cube the numbers 2nd tuple and print in tuple
n1=input("Enter a value:").split()
n2=input("Enter a value:").split()
from itertools import zip_longest
for i,j in zip_longest(tuple(n1),tuple(n2)):
    print((int(i)**2,int(j)**3))

#3)


    
