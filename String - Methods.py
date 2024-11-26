#string -->replace method

'''str1 = 'hello world hello'
print(str1.replace('l','L'))
print(str1.replace('hello','hai'))
print(str1.replace('l','L',1))
print(str1.replace('o','@',2))
print(str1) 

#string-->lower method
s_2 = input("Enter the string : \n")
print(s_2.lower())

#string-->upper method
s_1 = input("Enter the string : \n")
print(s_1.upper())0


#string-->swapcase method
s_1 = input("Enter the string : \n")
print(s_1.swapcase())

#string-->islower method
s_1 = input("Enter the string : \n")
print(s_1.islower())



#string-->isupper method
s_1 = input("Enter the string : \n")
print(s_1.isupper())

#string-->isalpha method
s_1 = input("Enter the string : \n")
print(s_1.isalpha())

#string-->isnumeric method
s_1 = input("Enter the string : \n")
`print(s_1.isnumeric())

#string-->isalnum method
s_1 = input("Enter the string : \n")
print(s_1.isalnum())

#string-->isspace method
s_1 = input("Enter the string : \n")
print(s_1.isspace())


#string -->startswith method
str1 = input("enter:")
sub_s = input("substring:")
print(str1.startswith(sub_s,0,len(str1)))

sub_s = input("substring:")
start_value = int(input("start_index:"))
print(str1.startswith(sub_s,start_value))


#string -->endswith method
str1 = input("enter:")
sub_s = input("substring:")
print(str1.endswith(sub_s,))
sub_s = input("substring:")
end_value = int(input("end_index:"))
print(str1.endswith(sub_s,0,end_value))


#string-->split method
str3 = "welcome to bangalore"
print(str3.split())

str3= "welcome to-bangalore"
print(str3.split())

str3= "welcome-to-bangalore"
print(str3.split())

#separator
str3= "welcome-to-bangalore"
print(str3.split('-'))
print(str3.split('to'))
print(str3.split('a'))

#maxsplit
str3= "welcome-to-bangalore"
print(str3.split('o'))
print(str3.split('o',1))
print(str3.split(' ',2))

#string-->rsplit method
'''str3 = "welcome to bangalore"
print(str3.rsplit())

str3= "welcome to-bangalore"
print(str3.rsplit())

str3= "welcome-to-bangalore"
print(str3.rsplit())

#separator
str3= "welcome-to-bangalore"
print(str3.rsplit('-'))
print(str3.rsplit('to'))
print(str3.rsplit('a'))

#maxsplit
str3= "welcome-to-bangalore"
print(str3.rsplit('o'))
print(str3.rsplit('o',1))
print(str3.rsplit('a',2))'''














