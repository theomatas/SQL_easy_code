import os, os.path

def my_write(filename,text): 

    path = filename
    file = open(path,'w')
    file.write(text)
    file.close()
    
    
def my_open(filename): 

    file = open(filename,'r')
    text = file.read()
    file.close()
    return (text)

def actualise(filename,text): 
    try:
        text = my_open(filename) + text
    except:
        pass
    my_write(filename,text)
    
def pwd(): 
    return os.path.dirname(__file__)


def ls(path): 
    return os.listdir(path)

