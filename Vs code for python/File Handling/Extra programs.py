#read from a file
'''def read_file():
    with open("file3","r")as file:
        content=file.read()
        print(content)
read_file()'''

#Append to a file
'''def append_to_file():
    with open("file2","a")as file:
        file.write("\nAppending a new line to the file.")
append_to_file()'''

#Read file line by line
'''def read_line_by_line():
    with open("file2","r")as file:
        line=file.readline()
        while line:
            print(line,end="")
            line=file.readline()
read_line_by_line()'''

#count number of lines in a file
'''def count_lines():
    with open ("file3","r")as file:
        lines=file.readlines()
        print(f"Number of lines:{len(lines)}")
count_lines()'''

#count words in a file
'''def count_words():
    with open("file2","r")as file:
        text=file.read()
        words=text.split()
        print(f"Number of words:{len(words)}")
count_words()'''


#check if file exists
'''import os
def check_file_exists(file_path):
    if os.path.exists(file_path):
        print("File Exist")
    else:
        print("File does not exist")
check_file_exists("file1")'''

#copy content from one file to another
'''def copy_file(source,designation):
    with open(source,"r")as src_file:
        content=src_file.read()
    with open(designation,"w")as dest_file:
            dest_file.write(content)
copy_file("file1","file5")'''

#find and replace text in a file
'''def find_and_replace(file_name,old_word,new_word):
    with open(file_name,"r")as file:
        data=file.read()
        new_data=data.replace(old_word,new_word)
    with open(file_name,"w")as file:
        file.write(new_data)
find_and_replace("file4","daughter","daughter(nainika)")
find_and_replace("file4","Police","DCP")'''

#Delete a file
'''import os
def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name}has been deleted.")
    else:
        print(f"{file_name}does not exist.")
delete_file("file5")'''

#count specific word in a file
'''def count_specific_word(word):
    with open("file3","r")as file:
        content=file.read()
        word_count=content.lower().split().count(word.lower())
        print(f"Occurences of '{word}'{word_count}")
count_specific_word("daughter")'''

#Reverse content of a file
'''def reverse_file_content(file_name):
    with open(file_name,"r")as file:
        content=file.read()
    with open(file_name,"w")as file:
        file.write(content[::-1])
reverse_file_content("file2")'''

#count number of characters in a file
'''def count_characters():
    with open("file3","r")as file:
        content=file.read()
        print(f"Number of characters:{len(content)}")
count_characters()'''

#read file into a list
'''def read_file_to_list():
    with open("file3","r")as file:
        lines=file.readlines()
        print(lines)
read_file_to_list()'''

#write a list to a file
'''def write_list_to_file(data_list):
    with open("file3","w")as file:
        for item in data_list:
            file.write(f"{item}\n")
write_list_to_file(["Apple","Banana","Orange"])'''

#move content one file to another
'''import shutil
def move_file(source,destination):
    shutil.move(source,destination)
    print(f"Moved{source} to {destination}")
move_file("file3","file5")'''

#write user input to a file
'''def write_user_input_to_file():
    user_input=input("Enter some text:")
    with open("user_input","w")as file:
        file.write(user_input)
write_user_input_to_file()'''\

#compare two files line by line 
'''def compare_files(file1,file5):
    with open(file1,"r")as f1,open(file5,"r")as f2:
        f1_lines=f1.readlines()
        f2_lines=f2.readlines()
        for line1,line2 in zip(f1_lines,f2_lines):
            if line1!=line2:
                print(f"Difference:{line1}!={line2}")
compare_files("file1","file5")'''

#Merge two files
'''def merge_files(file1,file5,output_file):
    with open(file1,"r")as f1,open(file5,"r")as f2,open(output_file,"w")as f_out:
        f_out.write(f1.read())
        f_out.write("\n")
        f_out.write(f2.read())
merge_files("file1","file5","merged_file")'''

#read a file in binary mode
'''def read_binary_file(file_name):
    with open(file_name,"rb")as file:
        content=file.read()
        print(content)
read_binary_file("file2")'''

#Pattern Matching
'''list_=["hello","hello world","hahaha","hehehe","hohohoho"]
patterns=["hello","world"]
matches=[]
for item in list_:
    for pattern in patterns:
        if pattern in item and item not in matches:
            matches.append(item)
print(matches)
    
            #list comprehension with any   
matches=[item for item in list_if any (pattern in item for pattern in patterns)]
print(matches)

            #List comprehension with All
matches=[item for item in list_if all (pattern in item for pattern in pattern)]
print(matches)
'''

#1)How many lines of data present in given file
'''with open('Example1.txt','r')as fo:
    data=fo.readlines()
print(len(data))'''

#2)How many words of data present in given file
'''with open('Example1.txt','r')as fo:
    data=fo.read().split()
print(len(data))'''

#3)How many lines of data present in given file with exactly 55 characters
count=0
with open('Example1.txt','r')as fo:
    for n in fo.readlines(): 
        data=n.strip()                    #error
        if len(data)==55:
          count+=1
print(count)

#4)Lengthiest word in the given file
'''with open('Example1.txt','r')as fo:
    file=fo.read().split()
    data=max(file,key=len) 
print(data)'''

#5)Lengthiest line in the given file
'''with open('Example1.txt','r')as fo:
    file=fo.readlines()
    data=max(file,key=len) 
print(data)'''

#6)print words which are starting with 'h'
'''with open('Example1.txt','r')as fo:
    file=fo.read().split()
    for i in file:
        if (i[0].lower()=='i'):
            print(i)'''
        

#7)print words which are having 10 characters in it
'''with open('Example1.txt','r')as fo:
    line=fo.read().split()
    for i in line:
        if len(i)==10:
            print(i)'''

