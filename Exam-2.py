'''1)
sentence="hello world welcome to python programming hi there"
d_={}
for word in sentence.split():
    if word[0] not in d_:
        d_[word[0]]=[word]
    else:
        d_[word[0]]+=[word]
print(d_)

2)
names=['apple','google','apple','yahoo','yahoo','google','gmail','gmail','gmail']
d_={}
for i,word in enumerate(names):
    if word not in d_:
        d_[word]=[i]
    else:
        d_[word]+=[i]
print(d_)'''

#3)
'''d={'a':'hello','b':100,'c':10.1,'d':'world'}
new_d={}
for key,value in d.items():
    if isinstance(value,str):
        d[key]=value[::-1]
    else:
        d[key]=value
print(d)'''

#4
'''files=['apple.txt','yahoo.pdf','gmail.pdf','google.txt','amazon.pdf','facebook.txt','flipkart.pdf']
d_={}
for file in files:
    f_=file.split('.')
    if(f_[1]=='txt'):
       d_['txt']=f_
    print(d_)
elif(f_[1]=='pdf'):
      print(f_)'''

#5
'''files=['apple.txt','yahoo.pdf','gmail.pdf','google.txt','amazon.pdf','facebook.txt','flipkart.pdf']
e1='txt'
e2='pdf'

file_={}
for file in files:
    f_e=file.split('.')
    if f_e[-1]==e1:
        if e1 not in file_:
            file_[e1]=[f_e[0]]
        else:
            file_[e1]+=[f_e[0]]
    elif f_e[-1]==e2:
        if e2 not in file_:
            file_[e2]=[f_e[0]]
        else:
            file_[e2]+=[f_e[0]]
print(file_)'''

#6)
'''for n in range(1,6):
  print(n * ' *')'''

#7)
l_=[4,5,1,6]
for i in enumerate(l_):
    l_.append(i[1] **i[0])
print(l_)
    




