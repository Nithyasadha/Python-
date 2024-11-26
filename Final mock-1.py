                                     #Functions
#User defined function
#1)sum of length
'''def len_():
    s_="work from home".split()
    su_=0
    for i in s_:
        l_=len(i)
        su_+=l_
    print(su_)
len_()'''

#2)check the argument passed more than 5
'''def f1(*a):
    if len(a)>5:
        print("True")
    else:
        print("False")
f1(2,4,5,77,12,4)
f1(2,34,56,90)'''

#3)func("TRACXN",0)#RCN  and  func("TRACXN",1)#TAX
'''def f1(s_,n):
    if n==0:
        print(s_[1::2])
    elif n==1:
        print(s_[0::2])
f1("TRACXN",0)
f1("TRACXN",1)'''
    
#4)High score with method and without method
'''def hi():
    n=2,67,12,99,234
    m=max(n)
    print(m)
hi()'''

'''num_=input("Enter:").split()
m_=0
for n in num_:
    if m_<int(n):
        m_=int(n)
print(m_)'''
    
#5)Average set of numbers


#6)Fizzbuzz
'''def func(num=int(input("Value:"))):
    if (num%3==0 and num%5==0):
        print("Fizzbuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    else:
        print("invalid")
func()'''
#7)clases attended and held -allowed to sit or not
#8)check perfect square or not

