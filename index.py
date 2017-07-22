#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
#form = cgi.FieldStorage()
print ("Content-Type: text/html")
print ()
print ("<html>")
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">')
print("""<head>
<style>
body  {
background-image: url("/files/background/1.jpg");
}
</style>
</head>""")
print("<body>")

#print('<div class="jumbotron">')
print('<div class ="container">')
print('<h2><br><font color="white">Face Recognition</font></h2>')
print('<form enctype="multipart/form-data" action="break.py" method="post">')
print('<div class="form-group">')#
#print('<label for="name"><font color="white">Name:</font></label>')
print('<input type ="text" name="name" class="form-control" placeholder="Enter Your Name" pattern="^[A-Za-z][A-Za-z0-9]*$"/>')
print('</div>')
print('<input type = "file" id="test_image" name = "fileName" value="" class="btn-info"/>')
print('<button type="submit" class="btn btn-primary">Upload</button>')
print("</form>")
print('<p><font color="white">PS: Name shouldnot contain blankspaces or special characters.</font></p>')
print('</div>')
#print('</div>')
print("""<div class="container">
<h2><font color="white">INFO:</font></h2>
<p class="lead"><font color="white">The name you fill will be used to verify the validity of the result produced by the Algorithm, improving it and fixing the bugs. Click on Train to train the system to recognize your face.</font></p>
<a href="upload.py" class="btn btn-info btn-lg btn-block"><font color="white">Train</font></a>
</div>""")
print('<br></div>')
print('<script src="js/jquery.min.js"></script>')
print('<script src="js/bootstrap.min.js"></script>')
print("</body>")
print("</html>")