#write()
'''with open ('file1','w') as f2:
    print(f2.write('how r u'))'''

'''with open ('file1','a') as f2:
    print(f2.write('hai'))'''

#writelines()
with open ('file1','a') as f2:
    print(f2.writelines('\n hai'))
    print(f2.writelines(['\n45','4.5','hey']))
    print(f2.writelines({'\n45':5,'0.5':34,'hello':4.5}))





