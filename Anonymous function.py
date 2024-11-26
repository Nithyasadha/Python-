                                   #<------Anonymous function=lambda--->
#1)program to square a number
'''n_=23,12,3,4,5,12
for i in n_:
  a_=i**2
  print(a_)'''

'''n_=lambda k:k*k
print(n_(6))'''


#2)program to find the square and cube
'''n_=lambda k:k*k
print(n_(6))
a_=lambda j:j**3
print(a_(3))'''

#3)program to check a character is vowel or not
'''ch_="ice"
v_='aeiou'
for i in ch_:
   if i in v_:
        print("vowel")
   else:
        print("Not")

v_=lambda x:"vowel" if x in 'aeiouAEIOU' else "Not"
print(list(map(v_,ch_)))'''

'''ch="vowel"
for i in ch:
    if i in 'aeiou':
        print("vowel")
    else:
        print("Not vowel")'''

'''n=lambda n:"vowel" if n in 'aeiou' else "not vowel"
print(list(map(n,ch)))'''




#4)program to check a character is even or not
'''str_="welcome"
for i in str_:
  if str_.index(i)%2==0:
         print("even")
  else:
       print("not")
l_=lambda n:"even" if str_.index(n)%2==0 else "not"
print(list(map(l_,str_)))
'''

        

#5)write a python program to create a lambda function that
#add 15 to a given number
'''n_=lambda n:n+15
print(n_(21))'''

#6)create lambda function that multiplies 2 arguments
'''a_=lambda i,j:i*j
print(a_(6,7))'''

#7)program to add 2 numbers
'''a_=lambda i,j:i+j
print(a_(12,9))'''

#8)program to solve a**2+b**2+2*a*b
'''a_=lambda a,b:a**2+b**2+2*a*b
print(a_(4,2))'''
#9)program to solve 2*a+3*b+4*c
'''a_=lambda a,b,c:2*a+3*b+4*c
print(a_(2,3,5))'''
#10)program to return last data of any sequence
'''num_=23,56,12,79,34
s_=lambda n:n[-1]
print(s_(num_))'''

#11)program to check if a string is palindrome or not
#num=input("Enter:")
'''n_=num[::-1]
if num==n_:
    print("Palindrome")                         #error
else:
    print("Not a palindrome")'''

'''n=lambda n:"palindrome" if num==num[::-1] else "Not"
print(list(map(n,num)))'''
#12)program to convert negative to positive number
'''num=[23,-2,0,42,-23,0]
for i in num:
    if i<0:
        print("Negative")
    elif i>0:
        print("Positive")
    else:
        print("Zero")'''

'''n=lambda i: "Positive" if i>0 else "Negative" 
print(list(n(num)))'''
#13)check a data is present in a list
#-------
#14)even or not in filter
#15)get all vowels in string
#16)check if string length is more than 5
#17)check if person age is 18 or more {'name':'Riya','age':20,'grade':'b'},
                #{'name':'nithya','age':23,'grade':'a'},
                #{'name':'sound','age':21,'grade':'b'},
                #{'name':'rudhresh','age':10,'grade':'a}










                     #<-------Filter-------->
#1)program to print only even numbers in the range 1 to 50
'''num_=filter(lambda i:i%2==0,(1,51))
print(num_)'''
#2)program to print only odd numbers in the range 1 to 50
'''for i in range(1,51):
    if i%2!=0:
        print(i)'''
'''pr=lambda i: i%2!=0  
print(list(filter(pr,range(1,51))))
pr=lambda i:i if i%2!=0 else "none"
print(list(map(pr,range(1,51))))'''
#3)Build a list with only even length string using filter func
#names=['apple','google','yahoo','facebook','yelp','filpkart','gmail','instagram','microsoft']
'''a_=n_.split()
for i in a_:
    if len(i)%2==0:
       print(i)'''
'''m_=lambda n:len(n)%2==0
print(list(filter(m_,names)))'''


#4)names=['laura','steve','bill','james','bob','greig','scott','alex','ive']
#Returns the string if the string is starting from vowel character
#names=['laura','steve','bill','james','bob','greig','scott','alex','ive']
'''for n in names:
    if n[0] in 'aeiouAEIOU':
        print(n)'''
'''a_=lambda n:n[0] in 'aeiouAEIOU'
print(list(filter(a_,names)))'''

#print(list(filter(lambda n:n[0] in 'aeiouAEIOU',names)))


#5)program to return only positive values in the list numbers=[-2,-1,-0,1,2]
'''numbers=[-2,-1,-0,1,2]
for j in numbers:
    if j>0:
        print(j)'''
'''n_=lambda j:j>0
print(tuple(filter(n_,numbers)))'''

#print(tuple(filter(lambda j:j>0,numbers)))

#6)program to print prime numbers from 1 to 50
'''s_=int(input("enter:"))
e_=int(input("Enter:"))
for n in range(s_,e_):
    if n<=1:
        pass
    else:
      for j in range(2,n):
        if n%j==0:
            break;
      else:
            print(n)'''
                                                                                #wrong
'''n_=lambda n:n%2!=0 
print(list(filter(n_,range(1,51))))'''
#7)program to extract only negative numbers from the list
#numbers=[-2,-1,-0,1,2]
'''for j in numbers:
    if j>0:
        print(j)'''
'''n_=lambda j:j>0
print(tuple(filter(n_,numbers)))'''

#print(tuple(filter(lambda j:j<0,numbers)))
























                             #<------Map------>
#1)convert uppercase
'''lis_=['guys','please','concentrate','in','the','class']
l_=str(lis_)
print(l_.upper())'''

'''lis_=['guys','please','concentrate','in','the','class']
li_=lambda l_: l_.upper()
print(list(map(li_,lis_)))
'''

#2)adding 2 lists element-wise
'''num1=[2,3,5,6]
num2=[5,7,8,32]
num_=lambda n,m:n+m
print(list(map(num_,num1,num2)))'''


#3)multiply 2 lists element-wise
'''num1=[2,3,5,6]
num2=[5,7,8,32]
num_=lambda n,m:n*m
print(list(map(num_,num1,num2)))'''


#4)converting list of integers into string
'''in_=34,12,67
print(str(in_))'''

'''in_=34,12,67
print(list(map(lambda k:str(k),in_)))'''
#5)mapping over a dictionary by increamenting each value by 1
#data={'a':1,'b':2,'c':4}
'''data={'a':1,'b':2,'c':4}
print(tuple(map(lambda data_:{data_[0]:data_[1]+1},data.items())))'''

    

#6)extract name field from dictionary
#students=[{'name':'Riya','age':20,'grade':'b'},


                #{'name':'nithya','age':23,'grade':'a'},
                #{'name':'sound','age':21,'grade':'b'},
                #{'name':'rudhresh','age':10,'grade':'a},]
'''students=[{'name':'Riya','age':20,'grade':'b'},
                {'name':'nithya','age':23,'grade':'a'},
                {'name':'sound','age':21,'grade':'b'},
                {'name':'rudhresh','age':10,'grade':'a'},]
print(list(map(lambda n:n['name'],students)))'''


#7)program to find square and cube of set of numbers
'''num_=[12,3,9,10,5,9]
for i in num_:
  n_=i**2
  print(n_)
  a_=i**3
  print(a_)'''

'''num_=[12,3,9,10,5,9]
m_=lambda j:j**3
print(list(map(lambda i:i**2,num_)))
print(list(map(lambda j:j**3,num_)))'''


#8)square the numbers and get only even numbers
'''st_va=int(input("Enter 1:"))
en_va=int(input("Enter 2:"))
r_=range(st_va,en_va+1)                                    #(1,8)
is_square=lambda n:n*n                                      #(1,4,9,16,25,36,49)
is_even=lambda e_n:e_n%2==0                         #(2,4,6)
print(list(map(is_square,filter(is_even,r_))))   '''      #(4,16,36)

#9)get length of all the strings in a tuple
'''t_=('what','about','your','health')
for i in t_:
  print(len(i))'''

'''t_=('what','about','your','health')
print(tuple(map(lambda n:len(n),t_)))'''

#10)rounding the numbers in set to 2 decimal point
'''floats={1.234,2.34,2.43,3.5,3.54,90.23}
for i in floats:
  print(round(i,2))'''

'''floats={1.234,2.34,2.43,3.5,3.54,90.23}
print(set(map(lambda n:round(n,2),floats)))'''

#11)program to reverse each list in tuple
'''tuple=[[3,2.4,2],[2.3,45,'12'],[34,12,2.3,True],[23,1]]
for i in tuple:
   print(i[::-1])'''

'''tupl_=[[3,2.4,2],[2.3,45,'12'],[34,12,2.3,True],[23,1]]
print(tuple(map(lambda n:n[::-1],tupl_)))'''

#12)program to square and cube every number in given list of integers

#13)program to find if a given string starts with given character

#14)program to convert negative numbers in given list to positive numbers

#15)program to return a list of elements raised to the power of their indices

#16)program to calculate sum of positive and negative numbers in a list



                             #<------sorted-------->

#1)program to sort below list
'''numbers1=[2,1,4,3,5,7,7,10]
print(sorted(numbers1))
print(sorted(numbers1,reverse=True))'''

#2)Program to sort according the length of string
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(sorted(random_words,key=len))'''

#3)sort according to 1st char
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(sorted(random_words))'''

#4)sort according to last char
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(sorted(random_words,key=lambda word:word[-1]))'''

#5)sort according to absolute value
'''complex_num=[3+4j,1-1j]
print(sorted(complex_num,key=abs))'''

#6)sorting a list of tuples by the second element
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(sorted(random_words,key=lambda word:word[-2]))'''

#7)sorting a dictionary by keys  #mydict={'banana':3,'apple':5,'cherry':2,'dates':4}
'''mydict={'banana':3,'apple':5,'cherry':2,'dates':4}
print(sorted(mydict.keys(),reverse=False))'''

#8)sorting a dictionary by values  #mydict={'banana':3,'apple':5,'cherry':2,'dates':4}
'''mydict={'banana':3,'apple':5,'cherry':2,'dates':4}
print(sorted(mydict.values(),reverse=False))'''

#9)sorting a list of dictionaries by a specific key
#student==[{'name':'Riya','age':20,'grade':'b'},
                #{'name':'nithya','age':23,'grade':'a'},
                #{'name':'sound','age':21,'grade':'b'},
                #{'name':'rudhresh','age':10,'grade':'a},]
'''student=[{'name':'Riya','age':20,'grade':'b'},
         {'name':'nithya','age':23,'grade':'a'},
         {'name':'sound','age':21,'grade':'b'},
         {'name':'rudhresh','age':10,'grade':'a'},]
print(sorted(student,key=lambda x:x['grade']))'''
   

#11)sorting with multiple keys   #error
'''student=[{'name':'Riya','age':20,'grade':'b'},
         {'name':'nithya','age':23,'grade':'a'},
         {'name':'sound','age':21,'grade':'b'},
         {'name':'rudhresh','age':10,'grade':'a'},]
print(sorted(student,key=lambda x:(x['name'],x['age'],x['grade'])))'''

#12)sorting a list of lists  #data=[1,2],[5,4],[2,3]
'''data=[1,2],[5,4],[2,3]
print(sorted(data,reverse=False))
#print(sorted(data,key=lambda x:x[0]))'''

#13)sorting a set of tuples by length of strings  #names={(bob,copper),(charley,Rakshit),(james,bond)}
'''names={('bob','copper'),('charley','Rakshit'),('james','bond')}
print(sorted(names,key=len))'''
#print(sorted(names,key=lambda x:x[0]))

'''import math
def f1():
    n=int(input("Enter:"))
    sq_=math.sqrt(n)
    if sq_==int(sq_):
        print("Perfect square")
    else:
        print("Not a perfect square")
f1()
       '''     


