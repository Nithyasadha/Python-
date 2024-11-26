'''b1,b2 = True,False
print(b1,b2)
print(type(b2))

print(bool())'''

#note
'''
print(bool(0),bool(34))
print(bool(0.0),bool(34.2))
print(bool(0j),bool(34+3j))
print(bool(False),bool(True))'''

#user input
#string
i = bool(input("Enter :"))
print(i, type(i))

#integer
i = bool(int(input("Enter:")))
print(i,type(i))

#float
a = bool(float(input("Enter:")))
print(a,type(a))

#complex
x = bool(complex(input("Enter:")))
print(x,type(x))



             


