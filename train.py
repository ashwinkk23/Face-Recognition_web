#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()
print("Content-Type: text/html")
print()
print('<html>')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">')
print("""<head>
<style>
body  {
background-image: url("/files/background/4.jpg");
}
</style>
</head>""")
print('<body>')
#print('<div class="jumbotron">')
print("""<br><br><div class="container">
<h2><font color="white">Login to proceed:</font></h2>
</div>
</div>
<div class="container">
<form action="login.py">
<div class="form-group">
<label for="email"><font color="white"></font></label>
<input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
</div>
<div class="form-group">
<label for="pwd"><font color="white"></font></label>
<input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pwd">
</div>
<button type="submit" class="btn btn-primary">Submit</button>
</form>
</div>""")
print('<script src="js/jquery.js"></script>')
print('<script src="js/bootstrap.min.js"></script>')
print('</body>')
print('</html>')