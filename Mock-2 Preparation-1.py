

                                   # Comprehension

#List comprehension                                   

#1)program to square the numbers in range
'''for i in range(1,11):
    print(i*2)'''
#print([i*2 for i in range(1,11)])
    
#2)program to square the numbers in range only which is even
#print([i*2 for i in range(1,11) if (i%2==0)])

#3)program to print "even" if numbers otherwise "odd"
#print(["even" if(n%2==0) else "odd" for n in range(1,11)])
#4)program to convert string to uppercase #words=(hello world python)
'''words=("hello world python").split()
print([j.upper() for j in words])'''

#5)program to fetch all the middle element in the lists
'''list_=[[1,2,3],['hi','bye','hello'],[12.3,1.5,90,300,23.1]]
for w_ in list_:
   li_=len(w_)//2
   print(w_[li_])'''

#print([w_[len(w_)//2] for w_ in list_])
#6)Extract digits from a string
'''text='a1b2c3'
for i in text:
    if i.isnumeric():
        print(i)'''

#print([i for i in text if i.isnumeric()])

#7)Create a list of tuples with number and its cubes
'''num_=[(1,4,5),(12,2,11)]
for j in num_:
    for i in j:
        print(i**3)'''
#print([i**3 for j in num_ for i in j])
#8)Filtering only numbers divible by 2 and 5
'''for num_ in range(1,51):
    if (num_%2==0 and num_%5==0):
        print(num_)'''

#print([num_ for num_ in range(1,51) if(num_%2==0 and num_%5==0)])
#9)Extract first letter of each word if it is consonent
'''a_="the gym was good to mens and womens".split()
for i in a_:
    if i[0] not in 'aeiouuAEIOU':
      print(i[0])'''

#print([i[0] for i in a_ if i[0] not in 'aeiouAEIOU'])
    
#10)Program to fetch the fruits and its indexes if the index odd
'''v_="banana","apple","grapes","papaya","orange"
for va_ in  v_:
    i_= v_.index(va_)
    if (i_%2!=0):
        print(i_,va_)'''

#print([va_ for va_ in v_ if(v_.index(va_)%2!=0)]) 
       

#11)Program to fetch only repeated characters in a string
'''v_="banana is a fruit"
v=' '
for i in v_:
    if v_.count(i)!=1:
       v+=i
print(v)'''

#print([i for i in v_ if v_.count(i)!=1])
  
    
    
#12)Create a list of dictionaries
'''keys = ['name','age','city']
values=['Dheena','26','salem']
d_={}
for i in range (len(keys)):
    d_[keys[i]]=values[i]
print(d_)'''

#13)Customizing numbers
#Creating a comprehension to print positive if the value is
#positive otherwise print negative if the value is negative
'''numbers=(-5,0,5,10,-10)
print(["Positive" if(n>=0) else "Negative" for n in numbers])'''


#14)Reverse a string if the length of string is more than 5
#otherwise print as it is
#v_="banana","apple","grapes","papaya","kiwi"
'''for i in v_:
    if len(i)>=5:
        print(i[::-1])
    else:
        print(i)'''
#print([i[::-1] if len(i)>=5 else i for i in v_])

#1)create a dictionary with word and its length
'''dict_={'banana':1,'apple':3,'orange':2}
d_={}
for i in dict_:
    d_[i]=len(i)
print(d_)'''

#print({i:len(i) for i in dict_})
#2)create a dictionary with character and its ascii value if the char is vowel
'''user_=input(" Enter:")
d_={}
for n in user_:
    if n in 'aeiouAEIOU':
        d_[n]=ord(n)
print(d_)'''

#print({n:ord(n)  for n in user_ if n in 'aeiouAEIOU'})
        
#3)create a dictionary with word and its length if the word length
#is less than 5 otherwise reverse the word
'''user_=input("Enter").split()
d_={}
for j in user_:
    if len(j)<5:
        d_[j]=len(j)
    else:
        d_[j]=j[::-1]
print(d_)

print({j:len(j) if len(j)<5 else j[::-1] for j in user_})'''

                                            #--->Arguments program<---
'''
1)check if the arguments that are passed more than 5
def f1(*a):
    if len(a)>=5:
        return True
    else:
        return False
print(f1(1,3,4,8))
print(f1(1,3,6,8,9))'''

#2)write a function to print below output
#func("TRACXN",0) #RCN
#func("TRACXN",1) #TAX
'''def f1(str_,n):
    if n==0:
        print(str_[1::2])
    elif n==1:
        print(str_[0::2])
f1("TRACXN",0)
f1("TRACXN",1)'''


              #<---Qtalk---->
#3)get highest score
#with method
'''user_=23,45,78,12,90,23
print(max(user_))'''

#without method
'''user_=23,45,78,12,90,23
max_=0
for n in user_:
   if (max_)<=n:
       max_=n
print(max_)'''

#2)average set of numbers   #wrong
'''he_=23,45,78,12,90,23
for i in he_:
   sum_=sum(i)
   l_=len(i)
print(sum_//l_)'''

#3)fizzbuzz
'''num=int(input("Enter:"))
if num%2==0 and num%5==0:
        print("Fizzbuzz")
elif num%2==0:
        print("fizz")
elif num%5==0:
        print("buzz")
else:
    print("Null")'''

#4)sit in exam or not
'''class_=int(input("Enter:"))
attended_=int(input("Enter:"))
per_=(attended_/class_)*100
if per_>=75:
    print("Allowed to sit ")
else:
    print("Not allowed to sit")'''

                                                         #-->Recursion<---
#1)Reverse a string
'''def f1(i=0,s_=' ',n=input("enter:")):  #recursion
  if i<len(n):
      s_=n[i]+s_
      return f1(i+1,s_,n)
  else:
      return s_
print(f1())'''

#2)get numbers from 1 to 5 and sum it
'''sum_=0
i=0
while i<=5:
    sum_+=i
    i+=1
print(sum_)'''

'''def f1(i=0,sum_=0):
    if i<=5:
        return f1(i+1,sum_+i)
    else:
        return sum_
print(f1())'''

#3)Factorial
'''n=int(input("enter:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)'''

'''def fun(i=1,fact=1,n=int(input("Enter:"))):
    if i<=n:
       fact=fact*i
       return fun(i+1,fact)
    else:
        return fact
print(fun())'''

#4)GCD
'''def fum(a,b):
    if b==0:
        return a
    else:
        return fum(b,a%b)
print(fum(5,25))'''
                                                     #-->function programs<---

'''import math
def f1():
    n=int(input("Enter:"))
    sq_=math.sqrt(n)
    if sq_==int(sq_):
        print("Perfect square")
    else:
        print("Not a perfect square")
f1()'''
            

   


        
    
    







    
    

        



