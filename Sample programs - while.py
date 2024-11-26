#1)Building a dictionary of word and length pair word-'This is a bunch of words'
'''s_='This is a bunch of words'
words_=s_.split()
w_=dict()
i=0
while i<len(words_):
    w_[words_[i]] = len(words_[i])
    i+=1
print(w_)

#2)Fliping keys and values of dictionary-dic = {'a':1,'b':4,'c':8}
dic = {'a':1,'b':4,'c':8}
items_=dic.items()
items_list = list(items_)
print(items_list)
d_={}
i =0
while i <len(items_list):
    d_[items_list[i][1]] = items_list[i][0]
    i+=1
print(d_)'''

#3)program to count the number of each character in a string
'''name = 'guido vann rossum'
d_=dict()
j=0
while j<len(name):
    d_[name[j]] = name.count(name[j])
    j+=1
print(d_)'''

#4)Program to create a dictionary with word and its count senten_="hello world welcome to python hello hi world welcome to java"
'''senten_="hello world welcome to python hello hi world welcome to java"
words_=senten_.split()
w_=dict()
i=0
while i<len(words_):
    word=words_[i]
    if word in w_:
        w_[word]+=1
    else:
        w_[word]=1
    i+=1
print(w_)
#5)Dictionary of character and ASCII value pair s = "absABS"
s_="absABS"
i=0
d_={ }
while i<len(s_):
      d_[s_[i]]=ord(s_[i])
      i+=1
print(d_)'''
#6)Building a dictionary whose price is greater than 200
#prices = {"AMEC":24.45, "APAL":612.45, "IBM":200.45,"HP":37.80, "FB":10.75}
'''prices = {"AMEC":24.45,
               "APAL":612.45,
               "IBM":200.45,
              "HP":37.80,
              "FB":10.75}
price_tuple = tuple(prices.items())
i = 0
d_price = {}
while i<len(price_tuple):
    if price_tuple[i][1]>200:
        d_price[price_tuple[i][0]] = price_tuple[i][1]
    i+=1
print(d_price)

#7)Program to get all the alphabets from string
s_="ashwin@345gmail.com"
i=0
a_=''
while i<len(s_):
    if (s_[i].isalpha()):
        a_+=s_[i]
    i+=1
print(a_)

#8)Program to get all the special characters from string
s_="ashwin@345gmail.com"
i=0
a_=''
while i<len(s_):
    if (not s_[i]. isalnum()):
        a_+=s_[i]
    i+=1
print(a_)'''

#9)Data = ['hi','hello','10','12.3',12,19,6.2] Program to get only integer from the list
data = ['hi','hello','10','12.3',12,19,6.2]
i=0
while i< len(data):
    if isinstance(data[i],int): 
      print(data[i])
    i+=1
#10)Program to print only vowels in a string s = "python,selenium"
'''s = "python,selenium"
i=0
s_=' '
while i<len(s):
    if (s[i] in ('a','e','i','o','u')):
        s_+=s[i]
    i+=1
print("Vowels in string:",s_)

#11)Program to get only alphanumeric characters in a string
st_=input("Enter a string:")
i=0
s_=' ' 
while i<len(st_):
  if (st_[i].isalnum()):
      s_+=st_[i]
  i+=1
print(s_)

#12)Write a program to check if the given list of string which is palindrome
p_=['123','121','dad','hello','hi']
i=0
while(i<len(p_)):
    if p_[i] == p_[i][::-1]:
        print(p_[i],",It is palindrome")
    else:
        print(p_[i],",It is not a palindrome")
    i+=1

#13)Replace all the vowels with star in the string = hello world
string = "hello world"
i=0
s_=' '
while i<len(string):
    if (string[i] in ('a','e','i','o','u')):
        s_+=string.replace(string[i],'*')
    i+=1
print("Vowels in string:",s_)


str_='python selenium'
in_=0
ne_s=' '
while in_<len(str_):
    if str_[in_] in 'aeiouAEIOU':
        ne_s=ne_s+'*'
    else:
        ne_s=ne_s+str_[in_]
    in_+=1
print(ne_s)'''

#14)Factorial number
num_=int(input("Enter a num:"))
i =1
fact_=1
while num_>=i:
    fact_=fact_*i
    i+=1
print("Factorial of ",num_,"is",fact_)
    



