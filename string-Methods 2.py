'''#string --> index method
str1 = input("enter :\n")
sub_string = input("Enter the sub_s:\n")
print(str1.index(sub_string))
sub_string = input("Enter the sub_s:\n")
str_index = int(input())
print(str1.index(sub_string,str_index))


str1 = input("enter :\n")
sub_string = input("Enter the sub_s:\n")
print(str1.index(sub_string))


#string-->find method
str1 = input("enter :\n")
sub_string = input("Enter the sub_s:\n")
print(str1.find(sub_string))
sub_string = input("Enter the sub_s:\n")
str_find= int(input())
print(str1.find(sub_string,str_find))


str1 = input("enter :\n")
sub_string = input("Enter the sub_s:\n")
print(str1.find(sub_string))


#string-->count method

str4 = "Good morning maam"
print(str4.count('o'))
print(str4.count('Good'))
print(str4.count('a'))
print(str4.count('123'))
print(str4.count('o',2))


#string-->strip method
str5 =input("enter:")
char_=input("enter:")
print(str5.strip(char_))



#string-->strip method
str5 =input("enter:")
char_=input("enter:")
print(str5.lstrip(char_)) 

#string-->strip method
str5 =input("enter:")
char_=input("enter:")
print(str5.rstrip(char_))'''


#string -->join method
#list
a_= ["a",'b',"7"]
print('  '.join(a_))
print(' -'.join(a_))
print(' 8'.join(a_))
print('  '.join(a_))
print(' i '.join(a_))

#tuple
t_=("a",'b',"7",'apple','6')
print('+'.join(t_))

#set
s_={"a",'b',"7",'apple','6'}
print('-'.join(s_))

#dict
d_={"a":9,'b':4.5,"7":6}
print('@'.join(d_))

#string
str_ ='hello'
print('_'.join(str_))




