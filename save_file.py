####save_file###
""" Saves the object"""
import pickle
def save(obj):
    """ Pickles the given object for future use"""
    file=open('Save.p','wb')
    pickle.dump(obj,file)
    file.close()

def load():
    return pickle.load(open('Save.p', 'rb'))

