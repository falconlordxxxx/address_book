######## Coworker########
""" Creates coworker object """
from base_file import base_class,create_new

class coworker(base_class):

    def __init__(self,name,phone_number,address,email,position):
        """ creates coworker object"""
        super (coworker,self).__init__(name,phone_number,address,email)
        self.position=position
    def __str__(self):
        return ' \
Name = {}\n\
Phone_Numbah={} \n\
Position={} \n\
email={} \n\
Address={}' .format(self.name,self.phone_numbah,self.position,self.email,self.address)





        
