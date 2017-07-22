#!/usr/bin/env python
from PIL import Image
import cgi
import os
import shutil
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
print ("Content-Type: text/html")
print ()
print ("<html>")
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">')
print("""<head>
<style>
body  {
background-image: url("/files/background/4.jpg");
}
</style>
</head>""")
print("<body>")
print('<br>')
image = form['fileName']
fn1 = os.path.basename(image.filename)
fn1 = fn1.split(" ")[0]
fn2 = os.path.basename(form.getvalue("name"))
img = fn2+'_'+fn1
if image.filename:
    if form.getvalue("name"):
        name = form.getvalue("name")
        print('<div class ="container">')
        print('<font color="white"><h2> Hello, {}</h2></font>'.format(name))
        print('<p><font color="white">Click proceed to proceed further.</font></p>')
        print('<form action="results.py" method="POST"')
        print('<p><input type="hidden" name="imgs" value={}/></p>'.format(str(img)))
        print('<button type="submit" class="btn btn-success">Proceed</button>')
        print('</div>')
        print('</form>')
    else:
        print('<div class ="container">')
        print('<p><font color="white">Please Enter your name</font></p>')
        print('<form action="index.py" method="post"')
        print('<input type="text" name="" value="">')
        #print('<input type="submit" value="Back"/>')
        print('<button type="submit" class="btn btn-warning">Back</button>')
        print('</form>')
        print('</div>')
else:
    print('<div class ="container">')
    print('<h1> Error </h1>')
    print('<p><font color="white">File not uplaoded.</font></p>')
    print('<p><font color="white">Click Back to try again</font></p>')
    print('<form action="index.py" method="post"')
    print('<input type="text" name="" value="">')
    #print('<input type="submit" value="Back"/>')
    print('<button type="submit" class="btn btn-warning">Back</button>')
    print('</form>')
    print('</div>')
image = form['fileName']
fn1 = os.path.basename(image.filename)
fn1 = fn1.split(" ")[0]
fn2 = os.path.basename(form.getvalue("name"))
img = fn2+'_'+fn1
try:
    with open('files/' + fn2+'_'+fn1, 'wb') as fout:#####################
        shutil.copyfileobj(image.file, fout)
except:
    print('<h1><font color="white">Error</font></h1>')
    print('<p><font color="white">File not uplaoded.</font></p>')
    print('<p><font color="white">click Back to try again.</font></p>')
    print('<form action="index.py" method="post"')
    print('<input type="text" name="" value="">')
    print('<input type="submit" value="Back"/>')
    print('</form>')
print('<script src="js/jquery.js"></script>')
print('<script src="js/bootstrap.min.js"></script>')
print("</body>")
print("</html>")