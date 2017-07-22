#!/usr/bin/env python
import sys
import os
from PIL import Image
sys.path.append('E:\\softwares\\xaamp\\htdocs\\files\\face')
from func_code import *
from func_code2 import *
from EigenfacesModel import *
from sklearn.externals import joblib
import cgi
import cgitb

cgitb.enable()
details = cgi.FieldStorage()
print("Content-Type: text/html")
print()
print('<html>')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">')
print('<body>')
if (details.getvalue("email")=="admin@admin.com")and(details.getvalue("pwd")=="python"):
    print('<div class="container">')
    [a,b] = update_db()
    print('<p>Building Model</p><br>')
    md = EigenfacesModel(a,b)
    print('<p>Saving Model</p><br>')
    os.chdir('E:\\softwares\\xaamp\\htdocs\\files')##########################
    joblib.dump(md, 'updated.pkl', compress=9)
    print('<p>Database Updated: Size {} MB</p>'.format((os.stat('updated.pkl').st_size)/(1024*1024)))
    print('</div>')
else:
    print('<div class="container">')
    print('<br><h2>Invalid Login</h2><br>')
    print('<a href="train.py" class="btn btn-danger" role="button">Back</a>')
    print('</div>')
print('<script src="js/jquery.js"></script>')
print('<script src="js/bootstrap.min.js"></script>')
print('</body>')
print('</html>')