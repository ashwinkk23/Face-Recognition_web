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
print("<body>")
print('<div class="jumbotron">')
print('<div class ="container">')
print("<h2><br>Face Recognition</h2>")
print('<form enctype="multipart/form-data" action="save_data.py" method="post">')
print('<div class="form-group">')#
print('<label for="name">Name:</label>')
print('<input type ="text" name="name" class="form-control" placeholder="Enter Your Name" pattern="^[A-Za-z][A-Za-z0-9]*$"/>')
print('</div>')
print('<input type = "file" name = "fileName" value="" class="btn btn-default"/>')
print('<button type="submit" class="btn btn-primary">Upload</button>')
print("</form>")
print('<p>PS: Name shouldnot contain blankspaces or special characters.</p>')
print('</div>')
print('</div>')
print("""<div class="container">
<h1>INFO:</h1>
<p class="lead">The name you fill will be used to verify the validity of the result produced by the Algorithm, improving it and fixing the bugs.</p>
<a class="btn btn-primary btn-lg btn-block">Learn More</a>
</div>""")
print('<script src="js/jquery.js"></script>')
print('<script src="js/bootstrap.min.js"></script>')
print("</body>")
print("</html>")