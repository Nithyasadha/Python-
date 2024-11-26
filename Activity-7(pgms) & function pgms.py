'''t_=(4,5,2,3,9,6,3,4)
print(min(t_))
print(max(t_))
print(sum(t_))'''

#1)Find the highest score in set of scores.Take the scores from user input
#a)Get the output with method
'''t_=(4,5,2,3,9,6,3,4)
print(max(t_))'''

#b)Get the output without method
'''num_=input("Enter some num:\n").split()
max_num=0
for num in num_:
    if int(num)>max_num:
        max_num=int(num)
print(max_num)'''

#2)Find the average set of numbers
#a)Get the output with method
'''heights={45,23,24,56,2}
sum_=sum(heights)
count_=len(heights)
print(f'The average :{sum_//count_}')'''

#a)Get the output without method
'''heights={34,12,67,34,90}
sum_,len_=0,0
for height in heights:
    sum_+=height
    len_+=1
print(f'The average :{sum_//len_}')'''

#3)Write a program to get fizzbuzz number
'''num_=int(input("Enter a number:"))
if (num_%3==0 and num_%5==0):
        print('fizz buzz')
elif (num_%3):
        print('fizz')
elif (num_%5):
        print('buzz')
        
num_=int(input("Enter a number:"))
for i in range(1,num_+1):
    if (i%3==0 and i%5==0):
        print('fizz buzz')
    elif (i%3):
        print('fizz')
    elif (i%5):
        print('buzz')'''
    
#4)Program to generate a password
'''from random import choice
alphabets=int(input("How many alphabets you need?"))
numbers=int(input("How many numbers you need?"))
special_char=int(input("How many special_char you need?"))

alpha_=' '
for a in range(ord('A'),ord('Z')+1):
        if chr(a).isalpha():
            alpha_+=chr(a)
            
numbers_=' '
for num in range(0,10):
    numbers_+=str(num)
    
special_char_='!@#$%^&*()'

password_=' '
for _ in range(1, alphabets+1):
               password_=password_+choice(alpha_)
               
for _ in range(1,numbers+1):
               password_=password_+choice(numbers_)
               
for _ in range(1,special_char+1):
               password_=password_+choice(special_char_)
               
shuffled_password=' '.join(set(password_))
print(f'Generater password is :{shuffled_password}')'''

'''import secrets
import string
import random
letters = string.ascii_letters
digits=string.digits
special_chars=string.punctuation
selection_list=letters+digits+special_chars
password_len=10
password=' '
for i in range(password_len):
    password+=' '.join(secrets.choice(selection_list))
print(password)'''

'''5)A school has folllowing rules for grading system
a)below 25 -F
b)25 to 45 -E
c)45 to 55 -D
d)50 to 60 -C
e)60 to 80 -B
f)above 80 -A
Ask the user to enter marks print the corresponding grade
tot_=int(input("Enter a total mark of student:"))
if tot_>=80:
        print('A')
elif 60<=tot_<=80:
        print('B')
elif 50<=tot_<=60:
        print('C')
elif 45<=tot_<=55:
        print('D')
elif 25<=tot_<=45:
        print('E')
elif tot_<=25:
        print('F')'''

'''A student will not be allowed to sit in the exam if his or her attendance is less than 75
Take following as input from user
a)no.of,classes held   b)no.of.classes.attended
print percentage of class attended and check whether the student is allowed to sit in the exam or not
class_=int(input("No.of.classes held :"))
attend_=int(input("No.of.classes.attended:"))
per_=(attend_/class_)*100
if per_<75:
        print("Not allowed to sit in the exam")
else:
        print("Allowed to sit in the exam")'''


                                #function programs


#1)Write a function to check if the number is Prime
'''def func():
  number=int(input("Enter a num:"))
  for n in range(2,number):
    if number%n == 0:
        break
  else:
        print("It is a prime number")
func()'''

#2)Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.
'''def last_():
        v_=int(input("Enter a value:"))
        a_=str(v_)
        print(int(a_[-1]))
last_()'''
#3)Make a function named tail that takes a sequence (like a list, string, or tuple)
#and a number n and returns the last n elements
#from the given sequence, as a list.  (#error)
'''def tail():
        l_=['hai','hello','good']
        st_="sweet","dreams"
        tu_=('welcome','to','salem')
        n_=int(input("Enter a number:"))
        n=l_,st_,tu_
        for i in n:
          print(i[-1])
tail()'''


#4)Write function named is_perfect_square that accepts a number
#and returns True if it's a perfect square and False if it's not.
'''import math
def is_perfect_square():
        num_=int(input("A number:"))
        sqrt_=math.sqrt(num_)             #17.0==17.0 is equal =>289
        if sqrt_==int(sqrt_):                  #3.8729==4.000 is not equal =>15
                print(sqrt_,"Perfect square")
        else:
                print(sqrt_,"Not a perfect square")
is_perfect_square()'''


#5)Write a function which returns the sum of lengths of all the iterables
'''def len_():
        s_="work from home".split()
        sum_=0
        for i in s_:
          l_=len(i)
          sum_+=l_
        print(sum_)
len_()'''
#6)Python function to check whether a number is Prime or not
'''def func():
  number=int(input("Enter a num:"))
  for n in range(2,number):
    if number%n == 0:
        print("It is not a prime number")
        break
  else:
        print("It is a prime number")
func()'''
#7)Python function  to check if a given number is Fibonacci number?'''
'''def fib_():
        val_=int(input("Value:"))
        a=0
        print(a)
        b=1
        print(b)
        for i in range(2,val_+1):
             c=a+b
             a=b
             b=c
             print(c)
fib_()'''
        
               
               





