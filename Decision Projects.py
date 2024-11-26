#DECISION STATEMENTS PROJECTS

#1)Enter marks and print the corresponding grades
'''n = int(input("Enter your mark:"))
if(n>=80):
        print("Grade of the student is A")
elif(60<=n<=80):
        print("Grade of the student is B")
elif(50<=n<=60):
        print("Grade of the student is C")
elif(45<=n<=50):
        print("Grade of the student is D")
elif(25<=n<=45):
        print("Grade of the student is E")
else:
        print("Grade of the student is F")


#2)take input of 3 peoples age and estimate
#oldest among them
n1 = int(input("Enter a age of 1st person:"))
n2 = int(input("Enter a age of 2nd person:"))
n3 = int(input("Enter a age of 3rd person:"))
if(n1>=n2 and n1>=n3):
    print("1st Person is oldest among them")
elif(n2>=n1 and n2>=n3):
    print("2nd person is oldest among them")
else:
    print("3rd person is oldest amoung them")

#youngest among them
n1 = int(input("Enter a age of 1st person:"))
n2 = int(input("Enter a age of 2nd person:"))
n3 = int(input("Enter a age of 3rd person:"))
if(n1<=n2 and n1<=n3):
    print("1st Person is youngest among them")
elif(n2<=n1 and n2<=n3):
    print("2nd person is youngest among them")
else:
    print("3rd person is youngest amoung them")


#3)student is allowed to sit in the exam or not
class_ =int(input("Number of classes:"))
attended_=int(input("Number of classes attended:"))
percentage =((attended_/ class_)*100)
print("Percentage:",percentage)
if(percentage>75):
    print("Sit in the exam")
else:
    print("not sit in the exam")


#random
import random
print(random.randint(1,10))
print(random.randint(50,60))
l_=[4,4.5,12,67]
index_=random.randint(a:0,len(l_)-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                                  bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb 0,len(l_)-1)
print(l_[index],"at the index",index_)

#choice
import random
places = ['goa','karnataka','tamilnadu','AP']
print(random.choice(places))
print("let's visit",random.choice(places))

#4)Program to get tail or head
import random
num_=random.randint(0,1)
if num_==0:
    print("head")
else:
    print("tail")
    
#5)program to guess a number
import random
name = input("What is your name:")
print("hey",name,"lets start the game")
computer_guess = random.choice((1,2,3,4,5,6,7,8,9,10))
user_guess = int(input("Guess a number:1 to 5"))
print(computer_guess)
if user_guess == computer_guess:
    print("you win")
elif user_guess<computer_guess:
    print("guess larger number")
elif user_guess>computer_guess:
    print("guess lower number")
else:
   print("guess only numbers in a tuple")

#6)Program stone,paper,scissor
import random
name = input("what is your name:")
print("hey",name,"Let's start the game")
computer_items = random.choice(['scissors','Rock','Paper'])
user_input = input("scissors or rock or paper:")
if computer_items == user_input:
    print('draw')
elif computer_items == 'scissor':
    if user_input == 'rock':
        print("you won rock hits scissor")
    else:
        print("you lost scissor cuts the paper")
elif computer_items == 'rock':
    if user_input == 'paper':
        print("you won paper wrap the rock")
    else:
        print("you lost,rock hits the scissor")
else:
    if user_input == 'scissor':
        print("you won,scissor cut the paper")
    else:
        print("you lost,paper wrap the rock") '''       




