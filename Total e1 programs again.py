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

'''i=0
while i<=5:
    print(i)
    i+=1

i=5
while i>=1:
    print(i)
    i-=1

i=1
while i<=10:
    print(i,"bangalore")
    i+=1

n=input("Name:")
m=int(input("Iteration:"))
i=1
while i<=m:
    print(n)
    i+=1

start_=int(input("Starting:"))
end_=int(input("Ending:"))
while start_<=end_:
    print(start_*start_)
    start_+=1

a=input("Enter:")
i=0
while(i<len(a)):
    print(i,a[i])
    i+=1

a=input("Enter:")
l_=[]
i=0
while(i<len(a)):
    l_+=[[a[i],ord(a[i])]]
    i+=1
print(l_)

value=input("Enter a value:")
v_=value.split()
i=0
while i<len(v_):
    print(v_[i],len(v_[i]))
    i+=1

num=input("value:")
if 'a'<=num<='z':
    print(chr(ord(num)-32))
elif 'A'<=num<='Z':
    print(chr(ord(num)+32))
else:
    print(num)

num=input("value:")
i=0
while i<len(num):
    if 'a'<=num[i]<='z':
        print(chr(ord(num[i])-32))
    elif 'A'<=num[i]<='Z':
        print(chr(ord(num[i])+32))
    i+=1

ls_= ['eve','james','bill','jome']
d_={}
i=0
while i<len(ls_):
    d_[ls_[i]] = ls_[i][0]
    i+=1
print(d_)'''





#1)building a dictionary of word and length pair word = "This is a bunch of words"
'''word = "This is a bunch of words"
w_=word.split()
dic={}
i=0
while i<len(w_):
    dic[w_[i]]=len(w_[i])
    i+=1
print(dic)'''


#2)flip keys and values of dictionary dictionary={'a':1,'b':4,'c':8}
'''dictionary={'a':1,'b':4,'c':8}
tu=tuple(dictionary.items())
d_={}
i=0
while i<len(tu):
    d_[tu[i][1]]=tu[i][0]
    i+=1
print(d_)'''
    

#3)count number of each character in string str1 = "guido vann rossum"
'''str1 = "guido vann rossum"
i=0
while i<len(str1):
    print(str1[i],str1.count(str1[i]))
    i+=1'''


#4)create dictionary with word and count senten_="hello world welcome to python hello hi world welcome to java"
'''senten_="hello world welcome to python hello hi world welcome to java"
s_=senten_.split()
d_={}
i=0
while i<len(s_):
    d_[s_[i]]=s_.count(s_[i])
    i+=1
print(d_)'''


#5)dictionary of character and ASCII value s="absABS"
'''s="absABS"
dic_={}
i=0
while i<len(s):
     dic_[s[i]]=ord(s[i])
     i+=1
print(dic_)'''


#X6)dictionary whose price value is more than 200 prices = {"AEMC":24.45,"APAL":612.45,"IBM":200.45,"HP":37.80,"FB":10.75}
'''prices = {"AEMC":24.45,"APAL":612.45,"IBM":200.45,"HP":37.80,"FB":10.75}
t_=tuple(prices.items())
d_={}
i=0
while i<len(t_):
    if t_[i][1]>200:
       d_[t_[i][0]]=t_[i][1]
    i+=1
print(d_)'''
        

#7)get all alphabets from string
'''str="hello123!@sdfg4567@#$"
i=0
s=' '
while i<len(str):
    if str[i].isalpha():
        s+=str[i]
    i+=1
print(s)
'''

#8)get all special character from string
'''str="hello123!@sdfg4567@#$"
i=0
s=' '
while i<len(str):
    if (not str[i].isalnum()):
        s+=str[i]
    i+=1
print(s)'''

#9)data=['hi','hello','10','12.3',12,19,6.2].get only integers from list
'''data=['hi','hello','10','12.3',12,19,6.2]
ls=[]
i=0
while i<len(data):
    if(isinstance(data[i],int)):
       print(data[i])
    i+=1'''

#10)print only vowels in string s="python,selenium"
'''s="python,selenium"
st=' '
i=0
while i<len(s):
    if s[i] in ('aeiouAEIOU'):
        print(s[i])
    i+=1'''

#11)get only alphanumeric character from string
'''str="hello123!@sdfg4567@#$"
st=' '
i=0
while i<len(str):
    if str[i].isalnum():
        print(str[i],end=' ')
    i+=1'''
        
#12)to check if list of string which is palindrome
'''list1=['mom','hey','goat','dad','wow']
i=0
while i<len(list1):
    p_=list1[i][::-1]
    if list1[i]==p_:
        print(list1[i],",palindrome")
    i+=1'''


#13)replace all vowels with star in string string = hello world
'''string ="hello world"
i=0
while i<len(string):
    if string[i] in ('aeiouAEIOU'):
        print(string.replace(string[i],'*'))
    i+=1'''



#1)lower to upper
'''string ="hello world"
print(string.upper())

#2)upper to lower
string ="hElLo wOrlD"
print(string.lower())

#3)upper to lower and lower to upper
string ="hElLo wOrlD"
print(string.swapcase())'''

#4)string in reverse
'''string ="hElLo wOrlD"
print(string[::-1])

string ="hello world"
i=0
while i<len(string):
    rev_=string[::-1]
    i+=1
print(rev_)'''


#5)length of string in list names=['eve','james','bill','steve','mill','amul']
'''names=['eve','james','bill','steve','mill','amul']
n_=[]
i=0
while i<len(names):
    n_.append(len(names[i]))
    i+=1
print(n_)'''


#6)1st character of each string in list names=['eve','james','bill','steve','mill','amul']
'''names=['eve','james','bill','steve','mill','amul']
s_=' '
i=0
while i<len(names):
    s_+=(names[i][0])
    i+=1
print(s_)'''



#7)end character of each string in list names=['eve','james','bill','steve','mill','amul']
'''names=['eve','james','bill','steve','mill','amul']
s_=' '
i=0
while i<len(names):
    s_+=(names[i][-1])
    i+=1
print(s_)'''


#8)dictionary with starting character and word in list names=['eve','james','bill','steve','mill','amul']
'''names=['eve','james','bill','steve','mill','amul']
d={}
i=0
while i<len(names):
    d[names[i][0]]=names[i]
    i+=1
print(d)'''

#9)dictionary with word and length word in list names=['eve','james','bill','steve','mill','amul']
'''names=['eve','james','bill','steve','mill','amul']
dt_={}
i=0
while i<len(names):
    dt_[names[i]]=len(names[i])
    i+=1
print(dt_)'''


#10)the words starting with vowel names=['eve','james','bill','steve','mill','amul']
'''names=['eve','james','bill','steve','mill','amul']
i=0
while i<len(names):
    if names[i][0] in ('aeiouAEIOU'):
       print(names[i])
    i+=1'''
        

#11)get the numbers of even l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
'''l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
    if l[i]%2==0:
        print(l[i],end=' ')
    i+=1'''


#12)get the numbers starting  of even l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
'''l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]
s=str(l[i])
i=0                                              #error
while i<len(l):
    if int(s[0])%2==0:
        print(s)
    i+=1

'''


#13)get the numbers ending with of odd l=[2,3,4,45,43,29,90,77,65,34,234,89,45,620]'''





#1)get 1 to 10
'''i=1
while i<=10:
    print(i)
    i+=1
#2)get -1 to -10
i=-1
while i>=-10:
    print(i)
    i-=1
#3)get 10 to 1
i=10
while i>=1:
    print(i)
    i-=1'''
#4)get 1 to input from user
num1=int(input("Enter:"))
num2=int(input("Enter:"))
i=num1
while num1<=num2:
     print(num1)
     i+=1
#5)get -20 to -10
'''i=-20
while i<=-10:
    print(i)
    i+=1
#6)get 1 to -10
i=1
while i>=-10:
    print(i)
    i-=1
#7)get -1 to 20
i=-1
while i<=20:
    print(i)
    i+=1
#8)get -10 to -1
i=-10
while i<=-1:
    print(i)
    i+=1'''



