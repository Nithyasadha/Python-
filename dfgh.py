#program to get middle word in list
'''list_=input("Enter:")
for word in list_:
   w_=len(word)//2            
   print(word[w_])'''

#program to get middle character of each word in list
'''list_=input("Enter:").split()
for word in list_:
   w_=(word[-1])            
   print(ord(w_))
'''
#create a set with number with square and cube
'''s={1,2,3,4,5}
s_=set()
for i in s:
    a,b=i**2,i**3
    s_.add((a,b))
print(s_)'''

def func():
  str_=int(input("start value:"))
  end_=int(input("end value:"))
  for i in range(str_,end_+1):
      if i<1:
          pass
      else:
          for j in range(2,i):
              if(i%j==0):
                  break;
          else:
                  print(i,"prime")
func()

