import os
import anydbm
import pickle

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)
            
  
if __name__ == '__main__':
    
    # cwd = os.getcwd()
    # walk(cwd)