#1)Reverse a string without method
'''n=input("Enter a string:")
st_=' '
i=0
while(i<len(n)):
    st_=n[i]+st_
    i+=1
print(st_)'''

'''def f1(i=0,s_=' ',n=input("enter:")):  #recursion
  if i<len(n):
      s_=n[i]+s_
      return f1(i+1,s_,n)
  else:
      return s_
print(f1())'''
#2)sum of digits                                                                    
'''num=int(input("Enter a number:"))
sum=0
for i in str(num):
    sum=sum+int(i)
print(sum)'''
#3)print multiplication table
'''for i in range(1,20+1):
    print('2 *',i,'=',2*i)'''
#4)counting characters which is vowel
'''va_=input("value:")
i=0
su=0
while i<len(va_):
    if va_[i] in ('aeiou'):
      su=su+1
    i+=1
print(su)'''
#5)generating a list of squares
'''n_=int(input("Enter:"))
l_=[]
for n in range(1,n_+1):
   l_.append(n**2)
print(l_)'''
#6)finding the largest number without method
'''v_1=int(input("v1:"))
v_2=int(input("v2:"))
v_3=int(input("v3:"))
if (v_1 >v_2) and (v_1>v_3):
    print("v1 is larger")
elif (v_1 <v_2) and (v_2>v_3):
    print("v_2 is larger")
else:
    print("v3 is larger")'''

'''v_=[12,102,34,345,67,90]
m_=v_[0]
for num in v_:
    if num>m_:
        m_=num
print(m_)'''
    

#7)counting occurences of each words in a string(user-input)
'''k_="hello world welcome hello to java welcome to python".split()
count_={}
for n in k_:
    if n in count_:
       count_[n]+=1
    else:
        count_[n]=1
print(count_)'''
    

#8)sum of series
'''sum=0
for i in range(1,10+1):
    sum+=i
print(sum)'''
    
#9)sum of even fibonacci numbers
'''n=int(input("Enter:"))
sum=0
a=0
b=1
print(a)
print(b)
for i in range(2,n):
        c=a+b
        a=b
        b=c
        if c%2==0:
            sum+=c
        print(c)'''
#10)removing duplicates without method
'''v=[1,2,5,7,9,1,2,7,2]
l=[]
for i in v:
    if i not in l:
        l.append(i)
print(l)'''
#11)counting negative numbers
'''v=[1,-2,5,-7,9,-1,-2,7,2]
s=0
for n in v:
    if n<0:
        print(n)'''

#12)identifying perfect squares in a range
'''for i in range(1,50+1):
    num=i**0.5
    if num==int(num):
        print(i)'''

#13)write a for loop to iterate through a dictionary and print keys with values greater than a threshold
#

'''scores={'alice':56,'bob':86,'charlie':78,'david':90}
threshold=80
for key,value in scores.items():
    if value>threshold:
        print(key)'''
    
#14)generating a list of cubes of odd numbers
'''num=5
cubes=[]
for i in range(1,num+1):
    if i%2!=0:
        cubes.append(i**3)
    print(cubes)'''
#15)pattern printing
'''            A
         A  C
       A C E
    A C E G
  A C E G I  '''
'''pattern="ACEGI"
for i in range(1,len(pattern)+1):
    print(pattern[:i])'''

'''s_=input("enter:")
si_=' '
i=0
while i<len(s_):
    si_=s_[i]+si_
    i+=1
print(si_)'''

'''s_=int(input("enter:"))
sum=0
for i in str(s_):
    sum+=int(i)
    print(sum)'''

'''for n in range(1,20+1):
    print('2 *',n,'=',2*n)'''

'''s_=input("enter:")
sum=0
for n in s_:
    if n in ('aeiou'):
        sum+=1
    print(sum)'''

'''s_=int(input("enter:"))
l_=[]
for k in range(1,s_+1):
    l_.append(k**2)
print(l_)'''

'''s_=[2,7,8,23,78]
max=s_[0]
for k in s_:
    if k>max:
        max=k
print(max)'''

'''s_=("hello hai hello python hai java").split()
l={}
for j in s_:
    if j in l:
        l[j]+=1
    else:
        l[j]=1
print(l)'''

'''sum=0
for n in range(1,10+1):
   sum+=n
print(sum)'''

'''n=int(input("Enter:"))
sum=0
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    if c%2==0:
        sum+=c
    print(c)'''

'''n=[12,34,21,21,56,34]
l=[]
for i in n:
    if i not in l:
        l.append(i)
print(l)'''

'''n=[12,-34,21,-21,-56,34]
for i in n:
    if i<0:
        print(i)'''

'''for i in range(1,10+1):
    num=i**0.5
    if num==int(num):
        print(i)'''

'''scores={'alice':56,'bob':86,'charlie':78,'david':90}
threshold=80
for key,value in scores.items():
    if value>threshold:
        print(key)'''




        
        



        


    




