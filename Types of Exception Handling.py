#1)default Exception handling(EH):
'''n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
try:
    print(n1/n2)
except Exception:
    print("numbers cannot divided by 0")'''

#2)Specified EH:
'''n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
try:
    print(n1/n2)
    d[[4,5]]=90
    print(d)
except ZeroDivisionError:
    print("Divided by 0")'''

#3)Multiple EH:
'''n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
d={}
try:
    print(n1/n2)
    d[[4,5]]=90
    print(d)
except ZeroDivisionError:
    print("Divided by 0")
except TypeError:
    print("keys must be immutable")'''

#4)Generic EH:
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
d={}
try:
    print(n1/n2)
    d[[4,5]]=90
    print(d)
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
