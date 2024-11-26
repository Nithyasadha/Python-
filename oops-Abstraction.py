                    #<--Abstraction-->

'''from abc import ABC,abstractmethod
class whatsappFrontend(ABC):
    def chat_box(self):
        pass
    def status_box(self):
        pass
    def call_window(self):
        pass
    def settings(self):
        pass
class whatsappBackend (whatsappFrontend):
    @abstractmethod
    def chat_box(self):
        print("Message sent")
    def status_box(self):
        print("display status")
    def call_window(self):
        print("calling")
    def settings(self):
        print("open settings")
try:
    user1=whatsappBackend()
    user1.chat_box()
except Exception:
    print("user not suppose")'''


              #<--custom exception handling-->
'''class AgeError(Exception):
    pass
age=int(input("what is your age?"))
if age>=18:
    print('Person is eligible')
else:
    raise AgeError("Person is not eligible")'''

'''class AgeError(Exception):
    pass
age=int(input("what is your age?"))
try:
    if age>=18:
        print('Person is eligible to vote')
    else:
        raise AgeError
except AgeError:
    print("person is not eligible to vote")'''


              















    
