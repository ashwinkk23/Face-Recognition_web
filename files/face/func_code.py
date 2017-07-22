import numpy as np
from PIL import Image
import os
from EigenfacesModel import *
from sklearn.externals import joblib
root = os.getcwd()

def create_db(path):
    os.chdir(path)
    X,y = [],[]
    sz = (370,470)
    try:
        for img in os.listdir(path):
            im = Image.open(img)
            im = im.resize(sz,Image.ANTIALIAS)
            im = im.convert('L')
            X.append(np.asarray(im,dtype=np.uint8))
            y.append(np.array(img.split('.')[0]))
    except:
        print("//")
    os.chdir(root)
    create_db(X,y)
    
def update_class():
    path = root + '/data_set'
    X,y = [],[]
    sz = (370,470)
    for dir in os.listdir(path):
        print(dir)
        if dir == 'data':
            os.chdir(path+'/'+'data')
            for img in os.listdir(path+'/'+'data'):
                try:
                    print(img)
                    im = Image.open(img)
                    im = im.resize(sz,Image.ANTIALIAS)
                    im = im.convert('L')
                    X.append(np.asarray(im,dtype=np.uint8))
                    y.append(np.asarray(img.split('.')[0]))
                    os.system('cls')
                except:
                    pass
        else:
            try:
                os.chdir(path+'/'+dir)
                try:
                    for img in os.listdir(path):
                        print(img)
                        im = Image.open(img)
                        im = im.resize(sz,Image.ANTIALIAS)
                        im = im.convert('L')
                        X.append(np.asarray(im,dtype=np.uint8))
                        y.append(np.asarray(dir))
                        os.system('cls')
                except:
                    print('//')
            except:
                pass
    return [X,y]
    
def save_class(X,y):
    mod = EigenfacesModel(X[0:],y[0:])
    joblib.dump(mod, 'database.pkl', compress=9)
    
def update_save_class(X1,y1,X2,y2):
    [X,y] = [X1+X2,y1+y2]
    create_db(X,y)
    
def load_database(dbname):
    mod = joblib.load(dbname)
    return mod
    
def create_db(X,y):
    mod = EigenfacesModel(X[0:],y[0:])
    joblib.dump(mod, 'database.pkl', compress=9)
    
def read_images(path):
    os.chdir(path)
    X,y = [],[]
    sz = (370,470)
    try:
        for img in os.listdir(path):
            print(img)
            im = Image.open(img)
            im = im.resize(sz,Image.ANTIALIAS)
            im = im.convert('L')
            X.append(np.asarray(im,dtype=np.uint8))
            y.append(np.array(img.split('.')[0]))
            os.system('cls')
    except:
        print("//")
    os.chdir(root)
    return [X,y]
    
def load_test(path):
    i = Image.open(path)
    sz = (370,470)
    i = i.resize(sz,Image.ANTIALIAS)
    i = i.convert('L')
    test = np.asarray(i,dtype=np.uint8)
    return test
    
def trial():
    return "working"