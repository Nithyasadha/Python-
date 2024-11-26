#WHILE LOOP
#program to print numbers from 1 to 5
'''i = 1
while(i<=5):
    print(i)
    i=i+1

#1)program to print numbers from 5 to 1
i = 5
while(i>=1):
    print(i)
    i-=1
        
#2)program to print "bangalore" 10 times
j=1
while j<=10:
    print("bangalore",j)
    j+=1

#3)program to print your name n times
j = 1
n = int(input("Enter a times:"))
while(j<=n):
    print("Nithya")
    j+=1

name = input("What is your name?")
count = int(input("give a count"))
i = 1
while(i<=count):
    print(name,i)
    i+=1

#4)program to square the number from start to end
a = int(input("Starting value:"))
b = int(input("Ending value:"))
while(a<=b):
    print(a*a)
    a+=1
    
#using append method
a = int(input("Starting value:"))
b = int(input("Ending value:"))
l_=[]
while(a<=b):
    l_.append(a*a)
    a+=1
    print(l_)

#using without append method
a = int(input("Starting value:"))
b = int(input("Ending value:"))
l_=[]
while(a<=b):
    l_=l_+[a*a]
    a+=1
    print(l_)

#5)program to get the characters and its indexes
value = input("Enter a value:")
start = 0
while(start < (len(value))):
    print(start,value[start])
    start+=1

    
#6)program to print nested list with character and its ASCII value
str_ = input("Enter a string:")
start = 0
l_ = []
while(start< len(str_)):
      l_+=[[str_[start],ord(str_[start])]]
      start+=1
      print(l_)

#7)program to get element and its length by taking the input from user
a_ = input("Enter a string:")
b_ = a_.split()
start = 0
while(start< len(b_)):
      print(b_[start],len(b_[start]))
      start+=1'''
      
                                               #QTALK programs
#1)Convert lowercase to upper
'''num1 = input("Enter a string:")
print(num1.upper())

#2)Convert uppercase to lower
num1 = input("Enter a string:")
print(num1.lower())

#3)Convert uppercase to lowercase and lowercase to uppercase with method
inp_ = input("Enter:")
if inp_.islower():
   print(inp_.upper())
else:
   print(inp_.lower())

#4)Convert uppercase to lowercase to lowercase to uppercase without using method
#(only convert the character )
num = input("Enter a string:")
i=0
a_=ord(num)
while(i<len(num)):
   b_=a_-32
   c_=chr(b_)
   print(c_)
   i=i+1

inp_=input("Enter:")
if 'a'<=inp_<='z':
   print(chr(ord(inp_)-32))
elif 'A'<=inp_<='Z':
   print(chr(ord(inp_)+32))
else:
   print("Invalid")

#5)Print indexes and characters of string
str_=input("Enter a string:")
i=0
while(i<(len(str_))):
  print("Index of a character is:",i,str_[i])
  i=i+1
  
#6)Convert uppercase to lowercase to lowercase to uppercase
  #without using inbuild method for more than one character
string_=input("Enter:")
index=0
new_str=' '
while index_<len(string_):
 if 'a'<=string_[index_]<='z':
   new_str+=(chr(ord(string_[index_])-32
 elif 'A'<=string_[index_]<='Z':
   new_str+=chr(ord(string_[index_])+32
 else:
   new_str+=string_[index_]
   index_+=1

#7)program to get the string in reverse order
inp_ = input("Enter a string:")
print(inp_[::-1])'''

'''inp_ = input("Enter a string:")
i = 0
n_s = ' '
while i<len(inp_):
  n_s = inp_[i]+n_s
  i+=1
print(n_s)'''

#8)program to get the length of a string in a list - names= ['eve','james','bill','steve','mill','amul']
#(find length of each word )
'''names= ['eve','james','bill','steve','mill','amul']
i=0
l_=[]
while(i<(len(names))):
  l_.append(len(names[i]))
  i=i+1
print(l_)

#9)Program to get the 1st character of each string in list- names= ['eve','james','bill','steve','mill','amul']
names= ['eve','james','bill','steve','mill','amul']
i=0
result=' '
while(i<(len(names))):
  result=(result+(names[i][0]))
  i=i+1
print("First character:\n",result)



#10)Program to get the end character of each string in list- names= ['eve','james','bill','steve','mill','amul']
names= ['eve','james','bill','steve','mill','amul']
i=0
result=' '
while(i<(len(names))):
  result=(result+(names[i][-1]))
  i=i+1
print("End character:\n",result)

#11)create a dictionary with starting character and word in list- names= ['eve','james','bill','steve','mill','amul'
names= ['eve','james','bill','steve','mill','amul']
dic_= {}
i = 0
while i<len(names):
  dic_[names[i][0]] = names[i]
  i +=1
  print(dic_)'''

#12)create a dictionary with word and length word in the list
'''names= ['eve','james','bill','steve','mill','amul']
dic_= {}
i = 0
while i<len(names):
  dic_[names[i]] = len(names[i])
  i +=1
print(dic_)

#13)print only the words starting with vowel-  names= ['eve','james','bill','steve','mill','amul']
names= ['eve','james','bill','steve','mill','amul']
i=0
word=' '
while i<len(names):
  if(names[i][0] in ('a','e','i','o','u','A','E','I','O','U')):
     word+=names[i]
  i+=1
print(word)'''

#14)Program to get the numbers which of even
'''l =[2,3,4,45,43,29,12,90,77,65]
i = 0
while i<len(numbers):
 if int(str(numbers[i])[0])%2==0:
    print(numbers[i])
 i+=1

#15)Program to get the numbers starting which of even
l =[2,3,4,45,43,29,12,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
    if l[i]%2==0:
        print(l[i])
    i+=1'''


#16)Program to get the numbers ending with odd number
'''l =[2,3,4,45,43,29,12,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
    if (l[i])%2!=0:
        print(l[i])
    i+=1'''

#-----#
#1)Program to get 1 to 10
'''i=1
while i<=10:
 print(i)
 i+=1

#2)Program to get -1 to -10
i=-1
while i>=-10:
     print(i)
     i-=1
 
#3)Program to get 10 to 1
i=10
while i>=1:
 print(i)
 i-=1

#4)Program to get 1 to user input
n=int(input("Number:"))
i=1
while i==n:
     print(i)
     i+=1

#5)Program to get -20 to -10
i=-20
while i<=-10:
     print(i)
     i+=1

#6)Program to get 1 to -10
i=1
while i>=-10:
     print(i)
     i-=1
     
#7)Program to get -1 to 20
i=-1
while i<=20:
     print(i)
     i+=1
     
#8)Program to get -10 to -1
i=-10
while i<=1:
     print(i)
     i+=1
'''
       

















    
    













