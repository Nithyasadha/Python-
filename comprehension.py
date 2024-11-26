                           #----->List and set comprehension<------#


#1)program to square the numbers in range 
'''list_=[]
for i in range(1,11):
        list_.append(i*i)
print(list_)'''

#---list comprehension--
#print([i*i for i in range(1,11) ])
#--set comprehension--
#print({i*i for i in range(1,11) })

#2)program to square the numbers in range only which is even
'''list_=[]
for i in range(1,11):
    if i%2==0:
        list_.append(i*i)
print(list_)'''

#---list comprehension--
#print([i*i for i in range(1,11) if i%2==0])
#--set comprehension--
#print({i*i for i in range(1,11) if i%2==0})

#3)program to print "even" if numbers otherwise "odd"

#---list comprehension--
#print(["even" if i%2==0 else "odd" for i in range(1,11)])
#--set comprehension--
#print({"even" if i%2==0 else "odd" for i in range(1,11)})

'''l_=[2,4,7,12,34]
print(["even" if i%2==0 else "odd" for i in l_])'''

#4)program to convert string to uppercase #words=(hello world python)
'''words='hello world python'.split()
for n in words:
  print(n.upper())'''

#---list comprehension--
#print([n.upper() for n in words])
#--set comprehension--
#print({n.upper() for n in words})


#5)program to fetch all the middle element in the lists
'''list_=input("Enter:").split()
for word in list_:
   w_=len(word)//2            
   print(word[w_])'''

'''list_=input("Enter:").split()
for word in list_:
   w_=(word[-1])            
   print(ord(w_))'''


#---list comprehension--
#print([word[len(word)//2]  for word in list_])'''
#--set comprehension--
#print({word[len(word)//2]  for word in list_})

#6)Extract digits from a string
#text='a1b2c3'
'''for i in text:
  if i.isnumeric():
     print(i)

print([i for i in text if i.isnumeric()])'''
#print({i for i in text if i.isnumeric()})

  
#7)Create a list of tuples with number and its cubes
#num_=[(1,4,5),(12,2,11)]
'''li_=[]
for i in num_:
   for j in i:
    li_.append(j**3)
print(li_)'''

#print([j**3 for i in num_ for j in i])
#print({j**3 for i in num_ for j in i})

#8)Filtering only numbers divible by 2 and 5
'''for i in range(1,21):
    if (i%2==0 and i%5==0):
        print(i)'''

#print([i for i in range(1,51) if i%2==0 and i%5==0 ])
#print({i for i in range(1,51) if i%2==0 and i%5==0 })

#9)Extract first letter of each word if it is consonent
'''a_="the gym was busy with spry owl kids".split()
l_=[]
for i in a_:
    if i[0] not in 'aeiou':            
       l_.append(i[0])
print(l_)'''

#print([i[0] for i in a_.split() if i[0] not in 'aeiou'])
#print({i[0] for i in a_.split() if i[0] not in 'aeiou'})
        
#10)Program to fetch the fruits and its indexes if the index odd
#v_="banana","apple","grapes","papaya","orange"
'''for n in v_:
    if v_.index(n)%2!=0:
        print(n)'''

#print([n for n in v_ if v_.index(n)%2!=0])
#print({n for n in v_ if v_.index(n)%2!=0})

#11)Program to fetch only repeated characters in a string
#v_="banana is a fruit"
'''l_=[]
for v in v_:    
    if v_.count(v)!=1:
        l_.append(v)
print(l_)'''

#print([v for v in v_ if v_.count(v)!=1])
#print({v for v in v_ if v_.count(v)!=1})

#12)Create a list of dictionaries
'''keys = ['name','age','city']
values=['Dheena','26','salem']
d_={}
for i in range(len(keys)):
   d_[keys[i]]=values[i]
print(d_)'''

#print([{keys[i]:values[i]}  for i in range(len(keys))])
#print({{keys[i]:values[i]}  for i in range(len(keys))})

#13)Customizing numbers
#numbers=(-5,0,5,10,-10)
#Creating a comprehension to print positive if the value is
#positive otherwise print negative if the value is negative
#numbers=(-5,0,5,10,-10)
'''for i in numbers:
  if i >=0:
     print("positive")
  else:
     print("negative")'''
  

#print(["positive" if(i>=0) else "negative" for i in numbers])
#print({"positive" if(i>=0) else "negative" for i in numbers})

#14)Reverse a string if the length of string is more than 5
#otherwise print as it is
#v_="banana","apple","grapes","papaya","kiwi"
'''for k in v_:
   if len(k)>5:
      print(k[::-1])
   else:
      print(k)'''

#print([k[::-1] if(len(k)>5) else k for k in v_])
#print({k[::-1] if(len(k)>5) else k for k in v_})






                      #------>Dictionary Comprehension<-----#

#1)create a dictionary with word and its length
''

d_={}
for i in dict_:
   d_[i]=len(i)
print(d_)'''

#print({i:len(i) for i in dict_})

#2)create a dictionary with character and its ascii value if the char is vowel
'''user_=input("Value:")
print({i:ord(i) for i in user_ if i in 'aeiou' })'''

#3)create a dictionary with word and its length if the word length
#is less than 5 otherwise reverse the word
user_=input("Enter:").split()
'''d_={}
for i in user_:
    if len(i)<5:
       d_[i]=len(i)
    else:
        d_[i]=i[::-1]
print(d_)'''
        
print({i:len(i) if len(i)<5  else i[::-1] for i in user_})

#4)


