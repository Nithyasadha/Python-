'''1 to 10
10 to 1
-10 to -1
-10 to 5
20 to -15
-20 to -15
even number '''

'''for i in range(1,11):
   print(i)

for i in range(10,0,-1):
  print(i)

for i in range(-10,0):
    print(i)

for i in range(-10,6):
    print(i)

for i in range(20,-16,-1):
    print(i)

for i in range(-20,-14):
    print(i)

x=int(input("Value:"))
for i in range(x):
    if i%2==0:
        print(i,"even number")'''

'''dict_={'asd':34,'df':45,'dfg':76}
for item in dict_.items():
  print(item[0],item[1])'''
  
'''for key in dict_.keys():
    print(key)

for value in dict_.values():
    print(value)

#break in 5
for i in range(1,10):
    if i==5:
        break
    print(i)

#continue
m_= 3,12,56,23,78,12,45
for n in m_:
  if n%2==0:
    continue
  print(n)

m_= 3,12,56,23,78,12,45
for n in m_:
    if(n=12):
        pass
  print(n)

str_=input("Enter:").split()
for n in enumerate(str_,1):
    print(n)'''

#----#
'''1)prime or not
2)prime or not in range
3)factorial
4)fibonacci number
5)armstrong number

num=int(input("Enter a value:"))
for i in range(2,num):
      if num%i==0:
        print("Not a prime")
        break
else:
    print("Prime")

st_=int(input("Enter :"))
en_=int(input("Enter:"))
for i in range(st_,en_+1):
    if i<=1:
      pass
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
                
num=int(input("Enter:"))
fact_=1
for i in range(fact_,num+1):
    fact_=fact_*i
print(fact_)

num=int(input("Enter:"))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c)'''

num=int(input("Enter:"))
n=len(str(num))
a=0
for digit in str(n):
       a+=int(digit)**n
    if (num==a):
        print("Armstrong")
    else:
        print("no armstrong")
    
    





