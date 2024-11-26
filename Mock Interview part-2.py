
                           ###Filter####



#1)program to square a number
#2)program to find the square and cube
#3)program to check a character is vowel or not
#4)program to check a character is even or not
#5)write a python program to create a lambda function that add 15 to a given number
#6)create lambda function that multiplies 2 arguments
#7)program to add 2 numbers
#8)program to solve a**2+b**2+2*a*b
#9)program to sove 2*a+3*b+4*c
#10)program to return last data of any sequence
#11)program to check if a string is palindrome or not
#12)program to convert negative to positive number
#13)check a data is present in a list
#-------
#14)even or not in filter
#15)get all vowels in string
#16)check if string length is more than 5
#17)check if person age is 18 or more {'name':'Riya','age':20,'grade':'b'},
                #{'name':'nithya','age':23,'grade':'a'},
                #{'name':'sound','age':21,'grade':'b'},
                #{'name':'rudhresh','age':10,'grade':'a}



                            ###Mapping#####



#1)convert uppercase
'''n="welcome"
print(n.upper())'''
'''n_=lambda n:n.upper()
print(tuple(map(n_,n)))'''
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
'''l1=4,2,667,24,12
print(str(l1))'''
#5)mapping over a dictionary by increamenting each value by 1
#data={'a':1,'b':2,'c':4}
'''d_=data.items()
dict_={}                           #another way
for i,j in d_:
   dict_[i]=j+1
print(dict_)'''

'''data={'a':1,'b':2,'c':4}      #correct method
d_=data.items()
dict_={}
for i in d_:
   dict_[i[0]]=i[1]+1
print(dict_)'''


'''dic_=lambda i: (i[0],i[1]+1)
print(dict(map(dic_,data.items())))'''
   

#6)extract name field from dictionary
#students=[{'name':'Riya','age':20,'grade':'b'},{'name':'nithya','age':23,'grade':'a'},{'name':'sound','age':21,'grade':'b'},{'name':'rudhresh','age':10,'grade':'a'}]
'''d_={}
for st in students:
     for i in st.items():
       if i[0]=='name':
                 d_[i[0]]=i[1]
     print(d_)'''

'''d_=lambda i: i['name']
print(list(map(d_,students)))'''

#7)program to find square and cube of set of numbers
#9)get length of all the strings in a tuple
#'t_=('what','about','your','health')
#10)rounding the numbers in set to 2 decimal point
#floats={1.234,2.34,2.43,3.5,3.54,90.23}
#11)program to reverse each list in tuple
#12)program to square and cube every number in given list of integers

#13)program to find if a given string starts with given character

#14)program to convert negative numbers in given list to positive numbers

#15)program to return a list of elements raised to the power of their indices

#16)program to calculate sum of positive and negative numbers in a list


                                   ###sorting####

#1)program to sort below list
'''numbers1=[2,1,4,3,5,7,7,10]
print(list(sorted(numbers1,reverse=False)))'''

#2)Program to sort according the length of string
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(list(sorted(random_words,key=len)))'''

#3)sort according to 1st char
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(list(sorted(random_words)))'''

#4)sort according to last char
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(list(sorted(random_words,key=lambda n:n[-1])))'''

#5)sort according to absolute value
'''complex_num=[3+4j,1-1j]
print(list(sorted(complex_num,key=abs)))'''

#6)sorting a list of tuples by the second element
'''random_words=['blank','spice','lion','hungry','cold','404','6lpa']
print(tuple(sorted(random_words,key=lambda n:n[-2])))'''

#7)sorting a dictionary by keys  #
'''mydict={'banana':3,'apple':5,'cherry':2,'dates':4}
print(list(sorted(mydict.keys())))'''

#8)sorting a dictionary by values  #
'''mydict={'banana':3,'apple':5,'cherry':2,'dates':4}
print(list(sorted(mydict.values())))'''
#9)sorting a list of dictionaries by a specific key
student=[{'name':'Riya','age':20,'grade':'b'},{'name':'nithya','age':23,'grade':'a'},{'name':'sound','age':21,'grade':'b'},{'name':'rudhresh','age':10,'grade':'a},]
print(list(sorted(student,keys
#11)sorting with multiple keys   #error
'''student=[{'name':'Riya','age':20,'grade':'b'},
         {'name':'nithya','age':23,'grade':'a'},
         {'name':'sound','age':21,'grade':'b'},
         {'name':'rudhresh','age':10,'grade':'a'},]'''
#12)sorting a list of lists  #data=[1,2],[5,4],[2,3]
#13)sorting a set of tuples by length of strings
#names={(bob,copper),(charley,Rakshit),(james,bond)}





