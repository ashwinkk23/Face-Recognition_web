import numpy as np
from PIL import Image
import os

def update_db():
    path = 'E:\\softwares\\xaamp\\htdocs\\files\\data_set'
    X,y = [],[]
    sz = (370,470)
    for dir in os.listdir(path):
        try:
            print(os.listdir(path))
            if dir == 'index.php':
                continue
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
                        #os.system('cls')
                    except:
                        pass
            else:
                os.chdir(path+'/'+dir)
                print(os.getcwd())
                try:
                    for img in os.listdir(os.getcwd()):
                        if img == 'index.php':
                            continue
                        print(img)
                        im = Image.open(img)
                        im = im.resize(sz,Image.ANTIALIAS)
                        im = im.convert('L')
                        X.append(np.asarray(im,dtype=np.uint8))
                        y.append(np.asarray(dir))
                        #os.system('cls')
                except:
                    print('Error')
        except:
            continue
    return [X,y]