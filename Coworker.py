######## Coworker########
""" Creates coworker object """
from base_file import base_class

class coworker(base_class):

    def __init__(self,name,phone_number,address,email,position):
        """ creates coworker object"""
        super (coworker,self).__init__(name,phone_number,address,email)
        self.position=position
    def getPosition(self): return self.position
    def setPosition (self,new_position):  self.position=new_position
    def __str__(self):
        return ' \
Name = {}\n\
Phone_Numbah={} \n\
Position={} \n\
email={} \n\
Address={}' .format(self.name,self.phone_numbah,self.position,self.email,self.address)

def coworker_var():
    """ Used to create instance  of coworker """
    name=input('Enter a name>>>')
    position=str(input('Enter a position>>>'))
    phone_number=str(input('Enter an phone number>>>'))
    address=str(input('Enter an address>>>'))
    email=str(input('Enter an email>>>'))   
    return coworker(name,phone_number,address,email,position)



        
