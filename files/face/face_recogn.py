import sys
import os
from func_code import *
from EigenfacesModel import *
from sklearn.externals import joblib
root = os.getcwd()
help ="""
Usage Syntax: python face_recogn.py [agrument] [String Content]

Positional Arguments:
--cdb : create database from image path
--ldb : load existing database from path
--udb : add person to database
--help : print this help and exit
"""
if sys.argv[1] == '--cdb':
    create_db(sys.argv[2])
    sys.exit()
    
if sys.argv[1] == '--ldb':
    md = load_database(sys.argv[2])
    os.chdir(root)
    test = load_test(sys.argv[3])
    print(md.predict(test))
    sys.exit()
    
    
if sys.argv[1] == '--udb':
    [a,b] = update_class()
    print('Building Model')
    md = EigenfacesModel(a,b)
    print('Saving Model')
    joblib.dump(md, 'database.pkl', compress=9)
    sys.exit()
    
if sys.argv[1] == '--help':
    print(help)
    sys.exit()