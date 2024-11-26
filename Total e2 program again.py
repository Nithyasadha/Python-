#1)prime or not
'''num=int(input("Enter:"))
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
        print("prime")'''


#2)prime or not in range
'''s_=int(input("start:"))
e_=int(input("end:"))
for i in range(s_,e_+1):
    if i<=1:
        pass
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
                print(i,"prime")'''




#3)factorial
'''s_=int(input("start:"))
fact_=1
i=1
while (i<=s_):
    fact_=fact_*i
    i+=1
print(fact_)'''


#4)fibonacci number
'''s_=int(input("start:"))
a=0
b=1
print(a)
print(b)
for i in range(2,s_):
    c=a+b
    a=b
    b=c
    print(c)'''


#5)armstrong number
s_=int(input("start:"))
a=len(str(s_))
n=0
for digit in str(s_):
       n+=int(digit)**a
if n==s_:
        print("armstrong")
else:
     print("not")
