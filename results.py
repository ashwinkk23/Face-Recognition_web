#!/usr/bin/env python
import cgi
import os
import shutil
import cgitb
import sys
sys.path.append('E:\\softwares\\xaamp\\htdocs\\files\\face')
from func_code import *
from EigenfacesModel import *
from sklearn.externals import joblib
cgitb.enable()
data = cgi.FieldStorage()
img_path = 'E:\\softwares\\xaamp\\htdocs\\files'
root = 'E:\\softwares\\xaamp\\htdocs'
print ("Content-Type: text/html")
print ()
print('<html>')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link href="css\\bootstrap.min.css" rel="stylesheet" media="screen">')
print("""<head>
<style>
body  {
background-image: url("/files/background/3.jpg");
}
</style>
</head>""")
print('<body>')
#
print("""<nav class="navbar navbar-toggleable-md navbar-light bg-faded">
<button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
</button>
<a class="navbar-brand" href="#">Face Recognition</a>
<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
<div class="navbar-nav">
<a class="nav-item nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
<a class="nav-item nav-link" href="#">Features</a>
<a class="nav-item nav-link" href="#">More</a>
<a class="nav-item nav-link" href="#">Feedback</a>
</div>
</div>
</nav>""")
#
print('<div class="jumbotron">')
print('<div class ="container">')
print('<div class="text-center">')
#print('<h1>Result</h1>')
print('</div>')
print('</div>')
#print(os.getcwd())#####################
print('<div class ="container">')
print('<div class="text-center">')
print('<h2>Are you...</h2>')
print('</div>')
#print(data.getvalue('imgs').split('/')[0])############################   Heroku
print('<div class="text-center">')
print('<br><img src= files\\'+data.getvalue('imgs').split('/')[0]+' class="img-thumbnail">')
print('</div>')
print('<br>')
os.chdir(img_path)
md = load_database('updated.pkl')
test = load_test(data.getvalue("imgs").split('/')[0])
print('<div class="text-center">')
#print('<h1>{}</h1>'.format(str(md.predict(test)).split('b')[1].upper().split('\'')[1]))
print('<h1>{}</h1>'.format(str(md.predict(test))).upper())
print('</div>')
os.chdir(root)
print('</div>')
print('<script src="js/jquery.js"></script>')
print('<script src="js/bootstrap.min.js"></script>')
print('</div>')
print('</body>')
print('</html>')