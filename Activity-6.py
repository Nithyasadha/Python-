#1)even or odd
'''num_ = int(input("Enter  a number:"))
condition_ = num_%2 ==0
if condition_:
  print("Even number")
else:
  print("Odd number")

#2)vowel or not
vowel_ = ('a','e','i','o','u')
n = input("Enter a value:")
if  n in vowel_:
    print("It is vowel")
else:
    print("It is consonent")

#3)Palindrome or not a palindrome in string
a = input("Enter a value:")
n = a[::-1]
if(a==n):
    print("Palindrome")
else:
    print("Not a palindrome")

#4)leap or not a leap year
year = int(input("Enter a year:"))
if (year%4==0 and year%100 ==0) or (year%400==0):
  print("Leap year")
else:
  print("Not a leap year")

#5)check perfect square or not
i = int(input("Enter:"))
s = i**0.5
if s*s == i:
        print(i,'is a perfect square')
else:
        print(i,'is not a perfect square')

#6)check alphabets or numbers or special character
n = input("Enter a value:")
if (n.isalpha()):
  print("It is alphabets ")
elif(n.isnumeric()):
  print("It is numeric")


char_=input("Enter ")
if len(char_)==1 and char_.isalpha():
  print('alphabet')
elif len(char_)==1 and char_.isnumeric():
  print('number')
elif len(char_)==1 and not char_isalnum():
  print('special character')
else:
  print("enter one character")

#7)pass if mark is greater than 35 else fail and
  #mark greater than 60 print first class
a = int(input("Enter a mark:"))
if (a>=60):
   print("1st class")
elif(35<=a and 60>=a):
    print("Pass")
else:
  print("Fail")

#8)starting character is vowel or not
s_=input("Enter a string:")
st_=s_[0]
if st_ in 'aeiouAEIOU':
   print("Vowel")
else:
  print("Not a vowel")

#9)list has even length or odd length
elements = input("Enter a elements:").split()
if len(elements)%2 ==0:
  print("Even length")
else:
  print("odd length")

#10)check dictionary is even print as it is
#otherwise add new key to make it even and print
dict_={'a':45,'b':'goat','c':'vijay'}
if len(dict_)%2 ==0:
  print(dict_)
else:
 dict_.update({'d':78})
 print(dict_)


 d = {}
 d.update({4:5,'a':4,'d':67})
 if len(d)%2==0:
   print(d)
 else:
  key = input("Enter key:")
  value = input("Enter value:")
  d[key] = value
  print(d)

#11)To check largest number in user input
n1 = int(input("Enter:"))
n2 = int(input("Enter:"))
n3 = int(input("Enter:"))
if(n1>=n2 and n1>=n3):
    print(n1,'is greaterst')
elif(n2>=n1 and n2>=n3):
    print(n2,'is greatest')
else:
    print(n3,'is greatest')

    #QTALK HOMEWORK 

#12)check if the first number is even or odd
num_ = input("Enter  a number:")
x = str(num_)
num1_ = x[0]
if int(num1_)%2==0:
  print(num1_,"Even number")
else:
  print(num1_,"Odd number")

#13)check the second last number is even or odd
num_ = input("Enter  a number:")
x = str(num_)
num1_ = x[-2]
if int(num1_)%2==0:
  print(num1_,"Even number")
else:
  print(num1_,"Odd number")'''
  
#14)check the datatype is string(mistake)
data_ =input("Enter:")
a=int(data_)
if isinstance(a,str):
    print("True")
else:
    print("False")
    
#15)check the datatype is float(mistake)


#16)check list is empty or not
'''list_=['gui',67]
if len(list_)==0:
    
    print("list is empty")
else:
    print("list is not empty")


#17)return the length of string if character are present
c_=input("Enter a string:")
if c_.isalpha():
    print("Present")
    print(len(c_))
else:
    print("Not present")

#18)program to get the last element in list
l1_=input("Enter a list:").split()
print(l1_[-1])

#19)program to get middle char in string
s1_=input("Enter a string:")
s2 = len(s1_)// 2
print(s1_[s2])

#20)program to check the data is number or special character
num = input("Enter a value:")
if (num.isnumeric()):
  print("Data is number")
elif(num.isalpha()):
    print("Data is different")
else:
    print("Data is special character")

#21)Program  to check the integer is positive or negative
num = int(input("Enter a number:"))
if(num>=0):
    print(num," is Positive")
else:
    print(num," is Negative")

#22)check smallest number in user input
a = int(input("Enter a num1:"))
b = int(input("Enter a num2:"))
c = int(input("Enter a num3:"))
if(a<=b and a<=c):
    print(a,"is smaller")
elif(b<=c and b<=a):
    print(b,"is smaller")
else:
    print(c,"is smaller")

#23)check tuple is empty or not
tup_=("form",67,"umbrella")
if len(tup_)==0:
    print("tuple is empty")
else:
    print("tuple is not empty")'''
    
#24)check the number is divisible by 5 or 8 and both
'''num = int(input("Enter a number:"))
if(num%5==0 and num%8==0):
    print(num,"Divisible by both 5 and 8")
elif(num%5==0): 
    print(num,"Divisible by 5")
elif(num%8==0):
    print(num,"Divisible by 8")
else:
    print("Invalid number")'''

#25)construct a marksheet using elif ladder
'''n = int(input("Enter your mark:"))
if(n>=80):
        print("Grade of the student is A")
elif(60<=n<=80):
        print("Grade of the student is B")
elif(50<=n<=60):
        print("Grade of the student is C")
elif(45<=n<=50):
        print("Grade of the student is D")
elif(25<=n<=45):
        print("Grade of the student is E")
else:
        print("Grade of the student is F")'''

#26)Take user input length and breadth of rectangle
#is equal print square or not(mistake) 





  
