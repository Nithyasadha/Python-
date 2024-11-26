'''data=['hi','hello','wow',10,'12.3',12,90,6.2]
i=0
while i<len(data):
    if(isinstance(data[i],int)):
        print(data[i])
    i+=1'''

'''data=['hi','hello','wow',10,'12.3',12,90,6.2]
i=0
while i<len(data):
    if(isinstance(data[i],int)):
        print(data[i])
    elif(isinstance(data[i],float)):
        print(data[i])
    i+=1'''

'''value=input("Enter:").split('.')
print(value[-1])'''

'''str_=("Hello welcome to python")
print(','.join(str_))'''

'''s="Sony12India567Pvt2ltd"
sum_=0
i=0
while i<len(s):
    if s[i].isnumeric():
        sum_+=int(s[i])
    i+=1
print(sum_)'''

'''a="SDFghjWjfER"
i=0
count=0
while i<len(a):
    if a[i].isupper():
        count=count+1
    i+=1
print(count)'''

'''s="@hello12world34welcome!123"
i=0
while i<len(s):
    if s[i].isalpha():
        print(s[i])
    elif not s[i].isalnum():
        print(s[i])
    i+=1'''

'''names=['apple','google','apple','yahoo','google']
i=0
s_=set()
du_=set()
while i<len(names):
    if names[i] in s_:
        du_.add(names[i])
    s_.add(names[i])
    i+=1
print(du_)'''

'''sentence='hello123world567welcometo9724python'
sum_=0
i=0
while i<len(sentence):
    if sentence[i].isnumeric():
        print(sentence[i])
        if int(sentence[i])%2==0:
              sum_+=int(sentence[i])
    i+=1
print("addition of even numbers",sum_)'''

'''d={'a':'hello','b':100,'c':10.1,'d':'world'}
k_=list(d.keys())
i=0
while i<len(k_):
    key=k_[i]
    if isinstance(d[key],str):
        d[key]=d[key][::-1]
    i+=1
print(d)'''

d={'a':'hello','b':100,'c':10.1,'d':'world'}
d_={}
k_=list(d.keys())
i=0
while i<len(k_):
    if isinstance(k_[i],str):
        d_[k_[i]]=d[k_[i]][::-1]
    i+=1
print(d_)
        

'''d={'a':100,'b':{'m':'man','n':'nose','0':'ox','c':'cat'}}
old_v='nose'
new_v='net'
i=0
while i<len(d['b']):
    j=0
    while j<len(d['b'][i]):
       if list(d['b'][i].values())[j]==old_v:
           d['b'][i][list(d['b'][i].keys())[j]]=new_v
       j+=1
    i+=1
print(d)'''
        
    

