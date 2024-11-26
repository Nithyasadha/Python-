#1)Program to print each line in the file
with open('Example1.txt') as f1:
    print(f1.readline())
    print(f1.readline())
    print(f1.readline())
    print(f1.readline())
    print(f1.readline())

#2)program to print the each line an line number in the file
'''with open('Example1.txt','r') as f1:
    for i,j in enumerate(f1,start=1):
        print(i,j) '''                               #correct

'''with open('Example1.txt') as f1:
    f1.seek(0)
    print(f1.tell())
    print(f1.readline())
    f1.seek(64)
    print(f1.tell())                                    #wrong
    print(f1.readline())
    f1.seek(128)
    print(f1.tell())
    print(f1.readline())
    f1.seek(195)
    print(f1.tell())
    print(f1.readline())
    f1.seek(262)
    print(f1.tell())
    print(f1.readline())'''

#3)Program to print last n lines in the file
'''with open('Example1.txt','r') as f1:
    file1=f1.readlines() 
    file=file1[-1]
    print(file)''' 

#4)program to count no of white spaces in the file 
'''with open('Example1.txt','r') as f1: 
    w_s=0
    for file in f1:
        for i in file:
            if i.isspace():
               w_s+=1
    print(w_s)'''    

#5)Program to print the words in the file
'''with open('Example1.txt','r') as f1:
    file1=f1.read()
    for i in file1.split():
        print(i) '''

#6)program to print the vowels in the file
'''with open('Example1.txt','r') as f1:
    file1=f1.read()
    for i in file1:
        if i in ('aeiouAEIOU'):
           print(i) '''       

#7)program to count no of vowels in the file
'''with open('Example1.txt','r') as f1:
    c_=0
    file1=f1.read()
    for i in file1:
        if i in ('aeiouAEIOU'):
          c_+=1
    print(c_)  '''

#8)program to count the occurance a particular word in the file
'''with open('Example1.txt','r') as f1:
    file=f1.read()
    file1=file.split()
    d_={}
    for i in file1:
        if i in d_:
             d_[i]+=1
        else:
             d_[i]=1
    print(d_)'''

#9)Program to print consonents in the file
'''with open('Example1.txt','r') as f1:
    file1=f1.read()
    for i in file1:
        if i not in ('aeiouAEIOU'):
           print(i)'''
#10)Program to print each line as element from the file
'''with open('Example1.txt','r')as f1:
    print(f1.readlines())'''
#11)program to print even lines in the file
'''with open('Example1.txt','r')as f2:
    for i,j in enumerate(f2):
      if i%2==0:
        print(j)'''

#12)program to print odd lines in the file
with open('Example1.txt','r')as f2:
    for i,j in enumerate(f2):
      if i%2!=0:
        print(j)

         

