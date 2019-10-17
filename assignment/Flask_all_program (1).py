# -*- coding: utf-8 -*


# Code => 1
from flask import Flask

app = Flask(__name__)

@app.route('/ChandraPrakash')

def index():
    return '''
<!DOCTYPE html>
<html>
<head>
	<title>Welcome1</title>
</head>
<body>
	<script type="text/javascript">
	var i = prompt("Enter your name => ");
	window.alert("Hello "+i);
</script>
</body>
</html>'''

if __name__ == '__main__':
    app.run()




# Code => 2
from flask import Flask

app = Flask(__name__)

@app.route('/Chandraprakash')

def index():
    return '''
<!DOCTYPE html>
<html>
<head>
	<title>welcome2</title>
</head>
<body>
	<section class="gmap">
		<div class="container">
			<div class="map">
				<iframe src="https://maps.google.com/maps?q=bsdu%20jaipur%20&amp;t=&amp;z=13&amp;ie=UTF8&amp;iwloc=&amp;output=embed"
				allowfullscreen style="width: 100%;height: 500px;">
				</iframe>
			</div>
		</div>
	</section>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBu-916DdpKAjTmJNIgngS6HL_kDIKU0aU&amp;callback=myMap"></script>
</body>
</html>'''

if __name__ == '__main__':
    app.run()
    
    
    
    

# Code => 3
from flask import Flask

app = Flask(__name__)

@app.route('/Chandraprakash')

def index():
    return '''
<!DOCTYPE html>
<html>
<head>
	<title>calculation of two num</title>
</head>
<body>

<script type="text/javascript">
	var i = parseInt(prompt("enter 1st number:"));
	var j = parseInt(prompt("enter 2nd number:"));
	var c = i + j;
	var d = i - j;
	var e = i * j;
	var f = i / j;
	document.write("Addition of the two number is: ",c,"</br>");
	document.write("Substraction of the two number is: ",d,"</br>");
	document.write("Multiply of the two number is: ",e,"</br>");
	document.write("Division of the two number is: ",f);
</script>

</body>
</html>'''

if __name__ == '__main__':
    app.run()
    
    
    
    
    
# Code => 4
from flask import Flask

app = Flask(__name__)

@app.route('/Chandraprakash')

def index():
    return '''
<!DOCTYPE html>
<html>
<head>
	<title>welcome3</title>
</head>
<body>
   
<h3>My name is Chandra prakash jeengar.I am student of ML & AI.</h3>
</body>
</html>'''

if __name__ == '__main__':
    app.run()
    
    
    
    
    
    
# Code => 5
from flask import Flask

app = Flask(__name__)

@app.route('/Chandraprakash')

def index():
    return '''
<!DOCTYPE html>
<html>
<head>
	<title>welcome4</title>
</head>
<body>
<h1>Hello, Mr. <span id="name"></span><br>
Welcome to the Bhartiya Skill Development University, Jaipur
</h1>
<script type="text/javascript">
	var i = prompt("Please enter your name:")
	document.getElementById('name').innerHTML=i;
</script>
</body>
</html>'''

if __name__ == '__main__':
    app.run()
    