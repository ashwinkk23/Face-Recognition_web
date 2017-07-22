#!/usr/bin/env python
import cgi
import cgitb
import shutil
import os
from PIL import Image

cgitb.enable()
new_data = cgi.FieldStorage()
print("Content-Type: text/html")
print()
print('<html>')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">')
print("""<head>
<style>
body  {
background-image: url("/files/background/7.jpg");
}
</style>
</head>""")
print('<body>')
if not (new_data.getvalue("Newname") and new_data.getvalue("Newemail")):
    print("""<div class="container">
        <br>
        <p><font color="white"><h2>Please Enter Name and Email. Click 'Back' to try again.</h2></font></p>
        <div class="container">
        <a href="upload_train_set.py" class="btn btn-warning" role="button">Back</a>
        </div>
        </div>
    """)
else:
    new_name = new_data.getvalue("Newname")
    new_email = new_data.getvalue("Newemail")
    try:
        os.mkdir('files/data_set/'+new_name)
    except:
        print('<div class="container">')
        print('<br><p><font color="white"><h5>Directory already exists.<br>Updating Existing Data.</h5></font></p>')
        print('</div>')
    if 'images_' in new_data:
        new_image = new_data["images_"]
    if not isinstance(new_image, list):
        new_image = [new_image]
    for image in new_image:
        if image.filename:
            fn = os.path.basename(image.filename)
            with open('files/data_set/'+new_name+'/'+fn,'wb') as fout:
                shutil.copyfileobj(image.file,fout)
    print('<div class="container">')
    print('<font color="white"><h3><br>Data uploaded successfully.<br>The database will be updated within 24 hours.</h3></font>')
    print('</div>')
#print('<script src="js/jquery.js"></script>')
print('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>')
print('<script src="https://npmcdn.com/tether@1.2.4/dist/js/tether.min.js"></script>')
print('<script src="https://npmcdn.com/bootstrap@4.0.0-alpha.5/dist/js/bootstrap.min.js"></script>')
#print('<script type="text/javascript" src="http://code.jquery.com/jquery-1.4.2.min.js"></script>')
print('<script src="js/bootstrap.min.js"></script>')
print('</body>')
print('</html>')