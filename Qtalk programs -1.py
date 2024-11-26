#1)program to print area of rectangle from user input
'''length_=int(input("Enter a length of rectangle:"))
width_=int(input("Enter a width of rectangle:"))
area = length_*width_
print("Area of the rectangle is:",area)

#2)program to square a number using user input
a_ = int(input("Enter a num:"))
sq_=a_*a_
print("Square of", a_ ,"is:",sq_)

#3)program to add a integer and a float
num_ = int(input("Number in int:"))
float_=float(input("Number in float:"))
add = num_+float_
print("Addition of integer and float:",add)

#4)program to find the square root
import math
x = int(input("The value of x is:"))
root_=math.sqrt(x)
print("The square root is:",root_)

#5)program  to add 2 numbers
a = int(input("Enter a:"))
b = int(input("Enter b:"))
add = a+b
print("Addition of a and b :",add)

#6)program to print a string 10 times
str = input("string:")
i = 0
while(i<=10):
   print(str,i)
   i=i+1

#7)program to combine 2 integer
x = int(input("Value of x :"))
y = int(input("Value of y :"))
combine_=str(x)+str(y)
print("The value of x and y is:",combine_)

#8)program to calculate area of triangle
b_ = int(input("Breadth:"))
h_=int(input("Height:"))
area = (1/2*b_*h_)
print("Area of the triangle:",area)

#9)program to convert kilometer to miles
kilo_ = int(input("Kilometer:"))
miles_ = kilo_/1.6093
print("Kilometer to miles:",miles_)'''

#10)program to convert any negative number to positive
num1 =int(input("Negative number:"))
positive_ = abs(num1)
print("Positive number:",positive_)


#11)program to convert integer to float
'''int_ = int(input("Integer:"))
float_=float(int_)
print("Integer to float:",float_)

#12)program to find the remainder and quotient
num1 = int(input("Enter a number1:"))
num2 = int(input("Enter a number 2:"))
quotient_=num1/num2
remainder_=num1%num2
print("Quotient =",quotient_)
print("Remainder =",remainder_)

n1 = int(input("num1:"))
n2 = int(input("num2:"))
print(divmod(n1,n2))
           
#13)program to round a number
m = 4.56
n = round(m)
print("Round of a number :",round(m))

#14)program to find the simple interest
p_=int(input("Principle:"))
n_ = int(input("Number of years:"))
r_=int(input("Rate of interest:"))
SI_=((p_*n_*r_)/100)
print("Simple interest = ",SI_)

#15)program to find the compund interest
p_=int(input("Principle:"))
n_ = int(input("Number of years:"))
r_=int(input("Rate of interest:"))
Amount_=(p_*((1+(r_/100))**n_))
CI_=(Amount_-(p_))
print("compound interest = ",CI_)'''



