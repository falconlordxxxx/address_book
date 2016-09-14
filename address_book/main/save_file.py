####save_file###
""" Saves the object"""
import pickle
from os import getcwd,chdir
def save(obj,obj_name):
    """ Pickles the given object in obj_name file for future use"""
    current_dir=getcwd()
    chdir('E:\AITEMP\\address_book\save')
    file=open(obj_name,'wb')
    pickle.dump(obj,file)
    chdir(current_dir)
    file.close()

def load(obj_name):
    """ Loads the file with obj_name and returns object on it"""
    current_dir=getcwd()
    chdir('E:\AITEMP\\address_book\save')
    a=pickle.load(open(obj_name, 'rb'))
    chdir(current_dir)
    return a



