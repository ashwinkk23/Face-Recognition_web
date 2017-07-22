import os
import numpy as np
from PIL import Image
import sys

root = os.getcwd()
def read_images(path,sz=None):
    c = 0
    X ,y = [] , []
    for dirname , dirnames , filenames in os.walk(path):
        for subdirname in dirnames :
            subject_path = os.path.join(dirname,subdirname)
        for filename in os.listdir(subject_path):
            try :
                im = Image.open(os.path.join(subject_path,filename))
                im = im.convert("L")
                if (sz is not None) :
                    im = im.resize(sz,Image.ANTIALIAS)
                X.append(np.asarray(im,dtype = np.uint8 ))
                y.append(c)
            except IOError :
                print ("I/O error ({0}) : {1} ". format ( errno , strerror ))
            except :
                print (" Unexpected error :", sys . exc_info () [0])
                raise
        c = c +1
    return [X , y]

def asRowMatrix (X) :
    if len (X) == 0:
        return np.array([])
    mat = np.empty((0 , X[0].size) , dtype = X[0].dtype)
    for row in X:
        mat = np.vstack((mat , np.asarray(row).reshape(1,-1)))
    return mat

def asColumnMatrix (X):
    if len (X) == 0:
        return np.array([])
    mat = np.empty ((X[0].size , 0) , dtype = X[0].dtype)
    for col in X:
        mat = np.hstack((mat , np.asarray(col).reshape(-1 ,1)))
    return mat

def pca(X , y , num_components =0):
    [n , d] = X.shape
    if ( num_components <= 0) or ( num_components >n) :
        num_components = n
    mu = X.mean( axis =0)
    X = X - mu
    if n > d:
        C = np.dot(X.T ,X)
        [eigenvalues,eigenvectors] = np.linalg.eigh(C)
    else :
        C = np.dot(X ,X .T)
        [eigenvalues,eigenvectors] = np.linalg.eigh(C)
        eigenvectors = np.dot (X .T , eigenvectors)
    for i in range (n):
        eigenvectors [: , i ] = eigenvectors [: , i ]/ np . linalg . norm ( eigenvectors [: , i ])
    idx = np.argsort ( - eigenvalues )
    eigenvalues = eigenvalues [ idx ]
    eigenvectors = eigenvectors [: , idx ]
    eigenvalues = eigenvalues [0: num_components ].copy ()
    eigenvectors = eigenvectors [: ,0: num_components ].copy ()
    return [ eigenvalues , eigenvectors , mu ]

def project (W , X , mu = None ):
    if mu is None :
        return np.dot(X ,W)
    return np.dot(X - mu , W)

def reconstruct (W , Y , mu = None ) :
    if mu is None :
        return np.dot(Y,W.T)
    return np.dot(Y,W .T) + mu

def normalize (X , low , high , dtype = None):
    X = np.asarray (X)
    minX , maxX = np.min(X) , np.max(X)
    X = X - float (minX)
    X = X / float ((maxX - minX))
    X = X * (high - low)
    X = X + low
    if dtype is None :
        return np.asarray(X)
    return np.asarray(X,dtype = dtype)

class AbstractDistance(object):
    def __init__(self , name):
        self._name = name
    def __call__ ( self ,p ,q):
        raise NotImplementedError (" Every AbstractDistance must implement the __call__method.")
    @property
    def name(self):
        return self._name
    def __repr__(self):
        return self._name
class EuclideanDistance(AbstractDistance):
    def __init__(self):
        AbstractDistance.__init__( self ,"EuclideanDistance")
    def __call__(self , p , q):
        p = np.asarray(p).flatten()
        q = np.asarray(q).flatten()
        return np.sqrt(np.sum(np.power(( p - q) ,2)))
class CosineDistance (AbstractDistance):
    def __init__(self):
        AbstractDistance.__init__(self,"CosineDistance")
    def __call__(self,p, q):
        p = np.asarray(p).flatten()
        q = np.asarray(q).flatten()
        return -np.dot(p.T,q)/(np.sqrt(np.dot(p,p.T )*np.dot(q,q.T)))

import numpy as np
class BaseModel(object):
    def __init__(self , X= None , y= None , dist_metric = EuclideanDistance () , num_components=0):
        self.dist_metric = dist_metric
        self.num_components = 0
        self.projections = []
        self.W = []
        self.mu = []
        if (X is not None ) and (y is not None ):
            self.compute(X,y)
    def compute(self,X,y):
        raise NotImplementedError("Every BaseModel must implement the compute method.")
    def predict(self,X):
        minDist = np.finfo('float').max
        minClass = -1
        Q = project(self.W , X.reshape(1,-1),self.mu)
        for i in range(len(self.projections)):
            dist = self.dist_metric(self.projections[i], Q)
            if dist < minDist:
                minDist = dist
                minClass = self.y[i]
        return minClass

class EigenfacesModel(BaseModel):
    def __init__(self , X= None , y= None , dist_metric = EuclideanDistance () , num_components=0):
        super(EigenfacesModel,self).__init__(X=X ,y=y , dist_metric = dist_metric,num_components=num_components)
    def compute(self,X,y):
        [D,self.W,self.mu] = pca(asRowMatrix(X),y,self.num_components)
        self.y = y
        for xi in X:
            self.projections.append(project(self.W,xi.reshape(1,-1),self.mu))

def read_my_imgs(path):
    os.chdir(path)
    X,y = [],[]
    try:
        for img in os.listdir(path):
            im = Image.open(img)
            im = im.resize(sz,Image.ANTIALIAS)
            im = im.convert('L')
            X.append(np.asarray(im,dtype=np.uint8))
            y.append(np.array(img.split('.')[0]))
    except:
        print("//")
    return [X,y]

def update_class():
    path = root +'/data_set'
    X,y = [],[]
    sz = (370,470)
    os.chdir(path)
    print(os.getcwd())
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
                    for img in os.listdir(os.getcwd()):
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
    os.chdir(root)
    return [X,y]