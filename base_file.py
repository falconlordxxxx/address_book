### Contacts_Manager

class base_class(object):

    def __init__(self,name,phone_numbah,address,email):
        self.name=name
        self.phone_numbah=phone_numbah
        self.address=address
        self.email=email
##Getters
    def getPhone_numbah(self):
        return self.phone_numbah
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getName(self):
        return self.name
##Setters
    def setPhone_numbah(self,new_numbah):
        self.phone_numbah=new_numbah
    def set_address(self,address):
        self.address=address
    def set_email(self,email):
        self.set_email=email
    def __str__(self):
        return ' \
Name = {}\n\
Phone_Numbah={} \n\
email={} \n\
Address={}' .format(self.name,self.phone_numbah,self.email,self.address)
##function for creating instance variable
def create_new():
    name=input('Enter a name>>>')
    phone_number=str(input('Enter an phone number>>>'))
    address=str(input('Enter an address>>>'))
    email=str(input('Enter an email>>>'))
    return name,phone_number,address,email

if __name__=='__main__':
    create_new()
