### Contacts_Manager

class base_class(object):

    def __init__(self,name,phone_numbah,address,email):
        self.name=name
        self.phone_numbah=phone_numbah
        self.address=address
        self.email=email

def create_new():
    """ creates instance variable for base_class"""
    name=input('Enter a name>>>')
    phone_number=str(input('Enter an phone number>>>'))
    address=str(input('Enter an address>>>'))
    email=str(input('Enter an email>>>'))
    return list(name,phone_number,address,email)

if __name__=='__main__':
    create_new()
