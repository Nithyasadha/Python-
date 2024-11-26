#Tell
'''with open('file1','r') as f3:
    print(f3.tell())'''
    
 #seek
'''with open('file1','r') as f3:   
    f3.seek(10)
    print(f3.read(10))
    print(f3.tell())'''

#create a file
'''with open('file3','x') as f4:
    print(f4)'''

#delete a file
import os
#print(os.remove('file2'))

#print(os.rename('file3','file2'))
print(os.replace('file3','file2'))



