'''list_=[5,6,7,7]
tuple_=(4.5,6.7)
print(len(list_),len(tuple_))

#'reusablity'
#1)Program to get length of any iterable with method
def length_(iterable):
    print(len(iterable))
 

length_([5,6,7,7])
length_((4.5,6.7))
length_('hai')'''

#2)Program to get length of any iterable without method
def length_(str_):
  count=0
  for i in str_:
     count+=1
  print(count)   

str_="goodmorningguys"
length_(str_)


