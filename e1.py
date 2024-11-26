'''1)print 1 to 5
2)print 5 to 1
3)print bangalore in 10 times
4)your name n times
5)square number from start to end
6)get characters and indexes
7)nested list with character and ascii value
8)get element and length by user input
9)uppercase to lowercase without method
10)uppercase to lowercase without using inbuild function
11)dictionary with starting character one word in list'''

i=0
while i<=5:
    print(i)
    i+=1


i=5
while i>=1:
    print(i)
    i-=1

i=1
while(i<=10):
    print("Bangalore",i)
    i+=1

n=input("Enter a value:")
m=int(input("Count is:"))
i=1
while(i<=m):
   print(n)
   i+=1

n=int(input("Enter a value:"))
 m=int(input("Enter a value:"))
i=n
while(i<=m):
   print(i*i)
   i=i+1

a=input("Enter a value:")
i=0
while i<len(a):
   print(a[i],i)
   i+=1
   
a=input("Enter a value:")
l_=[]
i=0
while i<len(a):
   l_+=[[a[i],ord(a[i])]]
   i+=1
print(l_)

a=input("Enter a value:")
b=a.split()
i=0
while i<len(b):
   print(b[i],len(b[i]))
   i+=1

a=input("Enter:")
if 'a'<=a<='z':
      print(chr(ord(a)-32))
elif 'A'<=a<='Z':
      print(chr(ord(a)+32))
else:
      print("invalid")'''

'''a=input("Enter:")
i=0
n=' '
while i<len(a):
  if 'a'<=a[i]<='z':
      n+=chr(ord(a[i])-32)
  elif 'A'<=a[i]<='Z':
      n+=chr(ord(a[i])+32)
  else:
     n+=a[i]
  i+=1
print(n)  '''    

'''a=input("Enter a value:")
d_={}
i=0
while i<len(a):
   d_[a[i][0]]=len(a[i])
   i+=1
print(d_)'''

'''1)lower to upper
2)upper to lower
3)upper to lower and lower to upper
4)string in reverse
5)length of string in list names=['eve','james','bill','steve','mill','amul']
6)1st character of each string in list names=['eve','james','bill','steve','mill','amul']
7)end character of each string in list names=['eve','james','bill','steve','mill','amul']
8)dictionary with starting character and word in list names=['eve','james','bill','steve','mill','amul']
9)dictionary with word and length word in list names=['eve','james','bill','steve','mill','amul']
10)the words starting with vowel names=['eve','james','bill','steve','mill','amul']
11)get the numbers of even l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
12)get the numbers starting  of even l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
13)get the numbers ending with of odd l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]'''


'''value=input("Enter:")
print(value.upper())

value=input("Enter:")
print(value.lower())

value=input("Enter:")
print(value.swapcase())

value=input("Enter:")
if value.islower():
   print("Lower")
elif value.isupper:
  print("Upper")
else:
  print("Invalid")

st_=input("value is:")
print(st_[::-1])

names=['eve','james','bill','steve','mill','amul']
s_=[]
i=0
while(i<len(names)):
  s_.append(len(names[i]))
  i+=1
print(s_)


names=['eve','james','bill','steve','mill','amul']
s_=' '
i=0
while i<len(names):
  s_+=names[i][0] 
  i+=1
print(s_)

names=['eve','james','bill','steve','mill','amul']
s_=' '
i=0
while i<len(names):
  s_+=names[i][-1]
  i+=1
print(s_)

names=['eve','james','bill','steve','mill','amul']
d_={}
i=0
while i<len(names):
  d_[names[i][0]] =names[i]
  i+=1
print(d_)

names=['eve','james','bill','steve','mill','amul']
d_={}
i=0
while i<len(names):
  d_[names[i]] =len(names[i])
  i+=1
print(d_)

names=['eve','james','bill','steve','mill','amul']
i=0
w_=' '
while i<len(names):
  if (names[i][0] in 'a,e,i,o,u,A,E,I,O,U'):
    w_+=names[i]
  i+=1
print(w_,end=' ')

l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
      if l[i]%2==0:
         print(l[i])
      i+=1

l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
      if l[i]%2==0:
         print(l[i])
      i+=1

l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
      if l[i]%2!=0:
         print(l[i])
      i+=1'''

'''1)get 1 to 10
2)get -1 to -10
3)get 10 to 1
4)get 1 to input from user
5)get -20 to -10
6)get 1 to -10
7)get -1 to 20
8)get -10 to -1
'''
'''i=1
while(i<=10):
  print(i)
  i+=1

i=-1
while i>=-10:
  print(i)
  i-=1

i=10
while i>=1:
  print(i)
  i-=1

hi=int(input("enter:"))
i=0
while(i<=(hi)):
     print(i)
     i+=1

i=-20
while i<=-10:
     print(i)
     i+=1

i=1
while(i>=-10):
     print(i)
     i-=1

i=-1
while(i<=20):
     print(i)
     i+=1

i=-10
while(i<=-1):
     print(i)
     i+=1'''

'''1)building a dictionary of word and length pair word = "This is a bunch of words"
2)flip keys and values of dictionary dictionary={'a':1,'b':4,'c':8}
3)count number of each character in string str1 = "guido vann rossum"
4)create dictionary with word and count senten_="hello world welcome to python hello hi world welcome to java"
5)dictionary of character and ASCII value s="absABS"
X6)dictionary whose price value is more than 200 prices = {"AEMC":24.45,"APAL":612.45,"IBM":200.45,"HP":37.80,"FB":10.75}
7)get all alphabets from string
8)get all special character from string
9)data=['hi','hello','10','12.3',12,19,6.2].get only integers from list
10)print only vowels in string s="python,selenium"
11)get only alphanumeric character from string
12)to check if list of string which is palindrome
13)replace all vowels with star in string string = hello world'''


'''word ="This is a bunch  of words"
s_=word.split()
d_={}
i=0
while(i<len(s_)):
     d_[s_[i]] = [len(s_[i])]
     i+=1
print(d_)

dict_={'a':1,'b':4,'c':8}
a_=dict_.items()
items_=list(a_)
d_={}
i=0
while(i<len(items_)):
     d_[items_[i][1]] = items_[i][0]
     i+=1
print(d_)

str1 = "guido vann rossum"
i=0
while i<len(str1):
     print(str1[i],str1.count(str1[i]))
     i+=1

s="absABS"
d_={}
i=0
while i<len(s):
     d_[s[i]]=ord(s[i])
     i+=1
print(d_)



alp_=input("Enter:")
i=0
while i<len(alp_):
     if alp_[i].isalpha():
          print("The Alphabets:",alp_[i])
     i+=1

alp_=input("Enter:")
i=0
while i<len(alp_):
     if  not alp_[i]. isalnum():
          print("The special characters:",alp_[i])
     i+=1

data=['hi','hello','10','12.3',12,19,6.2]
i=0
while(i<len(data)):
     if isinstance(data[i],int):
         print(data[i])
     i+=1

s="python,selenium"
i=0
while i<len(s):
     if (s[i] in( 'a','e','i','o','u','A','E','I','O','U')):
        print("vowels",s[i])
     i+=1

hi=input("Enter:")
i=0
while(i<len(hi)):
     if hi[i].isalnum():
          print(hi[i])
          i+=1
hello=['dad','wow','good','sweet','dreams']
i=0
while i<len(hello):
     pa_=hello[i][::-1]
     if(hello[i]==pa_):
          print(hello[i],"- palindrome")
          i+=1

string = "hello world"
i=0
while i<len(string):
     if string[i] in 'aeiouAEIOU':
          print(string.replace(string[i],'*'))
     i+=1

prices = {"AEMC":24.45,"APAL":612.45,"IBM":200.45,"HP":37.80,"FB":10.75}
t_=tuple(prices.items())
i=0
d_={}
while i<len(t_):
    if t_[i][1] > 200 :
          d_[t_[i][0]] = t_[i][1]
    i+=1
print(d_)'''

#--------#

