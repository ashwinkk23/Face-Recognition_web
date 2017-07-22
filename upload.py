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
background-image: url("/files/background/7.jpg");
}
</style>
</head>""")
print('<body>')
print("""
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script type="text/javascript" src="http://www.expertphp.in/js/jquery.form.js"></script>
<script>
function preview_images() 
{
var total_file=document.getElementById("images").files.length;
for(var i=0;i<total_file;i++)
{
$('#image_preview').append("<div class='col-md-3'><img class='img-responsive' src='"+URL.createObjectURL(event.target.files[i])+"'></div>");
}
}
</script>
</head>
<body>
<div class="container">
<br>
<font color="white"><h3>Upload 10 to 15 images of your face to train the system to recognize your face.</h3></font>
<div class="row">
<form action="_upload.py" method="post" enctype="multipart/form-data">
<div class="container">
<div class="form-group">
<label for="Newname"><font color="white"></font></label>
<input type ="text" class="form-control" placeholder="Enter Name" name="Newname">
</div>
</div>
<div class="container">
<div class="form-group">
<label for="Newemail"><font color="white"></font></label>
<input type="email" class="form-control" id="email" placeholder="Enter email" name="Newemail">
</div>
</div>
<div class="container">
<div class="col-md-6">
<div>
<input type="file" class="btn-info" id="images" name="images_1" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_2" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_3" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_4" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_5" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_6" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_7" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_8" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_9" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_10" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_11" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_12" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_13" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_14" onchange="preview_images();"><br>
<input type="file" class="btn-info" id="images" name="images_15" onchange="preview_images();"><br>
</div>
</div>
</div>
<div class="container">
<div class="col-md-6">
<input type="submit" class="btn btn-primary" name='submit_image' value="Submit Data"/>
</div>
</div>
</form>
</div>
<div class="row" id="image_preview"></div>
</div>
</div>""")
print('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>')
print('<script src="https://npmcdn.com/tether@1.2.4/dist/js/tether.min.js"></script>')
print('<script src="https://npmcdn.com/bootstrap@4.0.0-alpha.5/dist/js/bootstrap.min.js"></script>')
print('</body>')
print('</html>')