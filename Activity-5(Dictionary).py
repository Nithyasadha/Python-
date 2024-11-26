#1)Increament the value 'b'
point={'a':1,'b':2,'c':4}
if('b' in point):
    point['b']+=1
else:
    point[b]=1
print(point)

#2)difference of pop item and pop
#pop items
dic_={'a':78,56:'hi','g':'hai',67:46}
dic_.popitem()
print(dic_)

#pop
dic_={'a':78,56:'hi','g':'hai',67:46}
dic_.pop('a')
print(dic_)

#3)dictionary with 'o' as value for all the keys
l_=['a','b','c','e']
print(dict.fromkeys(l_,'o'))

#4)Merge two dictionary
d1={'a':78,56:'hi','g':'hai',67:46}
d2={'sun':'moon',67:78,'good':23,55:'morning'}
print(d1|d2)
