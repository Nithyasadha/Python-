'''str1 = "b@ng@!0r3"
print(id(str1))
print(str1,len(str1))

#indexing
#starting character

print(str1[0],str1[-9],str1[-len(str1)])

#ending character

print(str1[8],str1[len(str1)-1],str1[-1])

#if characters are same
#the address will be same

print(id(str1[1]),id(str1[4]))

#program to get the middle
str1 = "B@ng@!0r3"
middle_index = len(str1)//2
print(middle_index, str1[middle_index])

#getting input
str1 = input("Enter :")
middle_index = len(str1)//2
print(middle_index,str1[middle_index])'''


#program to get the last 2 characters
str2 = input("Enter: ")
print(str2[len(str2)-2])

#shortcut
str2 = input("Enter: ")
print(str2[-2])
