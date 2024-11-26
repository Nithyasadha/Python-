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
alphabets=input("How many alphabets you need?")
numbers=input("How many numbers you need?")
special_char=input("How many special_char you need?")

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
print(f'Generater password is :{shuffled_password}')

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







               
               





