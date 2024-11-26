#1)Program to print numbers from 10 to 10
'''def print_(i=1,l_=[]):
    if i<=10:
        l_.append(i)
        return print_(i+1,l_)
    else:
        return l_
print(print_())'''

#2)Program to print numbers from 20 to 10
'''def print_(i=20,l_=[]):
    if i>=10:
        l_.append(i)
        return print_(i-1,l_)
    else:
        return l_
print(print_())'''

#3)Program to get numbers from 1 to 5 and sum it 
'''def print_(i=1,l_=[],sum_=0):
    if i<=5:
        l_.append(i)
        return print_(i+1,l_,sum_+i)
    else:
        return sum_
print(print_())'''

#4)Program to get factorial of a number
'''def print_(i=1,fact_=1):
  if i<=5:
    fact_=fact_*i
    return print_(i+1,fact_)
  else:
     return fact_
print(print_())'''

#5)Program to get sum of digits
'''def print_(n):
    if n<10:
        return (n)
    else:
        return n%10 + print_(n//10)      #(345)n%10=>take last digit=5
print(print_(345))'''                            #(345)n//10=>removes last digit=return(34

#6)Program to reverse a string
'''def fun_(i=0,n_s=' ',str_=input("Enter a string:")):
  if(i<len(str_)):
         n_s = str_[i]+n_s                  #i=0  n_s=' '  str_='hai'
                                                    #n_s='h'+' '
         return fun_(i+1,n_s,str_)       #i=1  n_s='h'
                                                      #n_s='a'+'h'
  else:                                         #i=2  n_s='a'
                                                    #n_s='i'+'ha
                                                   
        return n_s
print(fun_())'''


#7)Greatest common Divisor
'''def gcd(a,b):
    if b==0:                                     
        return a
    else:
        return gcd(b,a%b)
print(gcd(35,10))'''

'''(a=25,b=5)
if b==0:
---                                              
else:
   gcd(b,a%b)
        (5,25%5)
        (5,0)
----next iteration----
(a=5,b=0)
if b==0:
  return a
  return (5)
-----'''


#8)Program to convert uppercase each words in a tuple
#9)Fibonacci sequence
def fun(n):      #error
    a,b=0,1
    for i in range(n):
      a,b =b,a+b
    return a
num_=int(input("Enter a number:"))
print(fun(num_))


    
