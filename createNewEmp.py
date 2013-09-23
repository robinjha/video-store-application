import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def run():
    try:
        http_headers()
        print """
			<html>
			<head>
			
			<title>Create New Employee</title>

			<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
			<script src="http://code.jquery.com/jquery-latest.js"></script>
			
			<script type="text/javascript"> 
			$(document).ready(function(){
			$(".flip").click(function(){
				$(".panel").slideToggle("slow");
			  });
			});
			</script>
			 
			<style type="text/css"> 
			div.panel,p.flip
			{
			margin:0px;
			padding:5px;
			text-align:center;
			background:#e5eecc;
			border:solid 1px #c3c3c3;
			}
			div.panel
			{
			height:500px;
			display:none;
			}
			
			</style>
			</head>
			 
			<body>
			 
			<div class="panel">
			<fieldset id="signin_menu">
					<form>
					  <label for="username">Username (E-mail Address)</label>
					  <input id="username" name="username" value="" title="username" type="text">

					  </p>
					  <p>
						<label for="password">Password</label>

						<input id="password" name="password" value="" title="password" tabindex="5" type="password">
					  </p>
					  
					  <p>
						<label for="firstname">FirstName</label>

						<input id="firstname" name="firstname" value="" title="firstname" tabindex="5" type="text">
					  </p>
					  
					  <p>
						<label for="lastname">LastName</label>

						<input id="lastname" name="lastname" value="" title="lastname" tabindex="5" type="text">
					  </p>
					  
					  <p>
						<label for="phonenum">Phone Num</label>

						<input id="phonenum" name="phonenum" value="" title="phonenum" tabindex="5" type="text">
					  </p>
					  
					  <p>
						<label for="address">Address</label>

						<input id="address" name="address" value="" title="address" tabindex="5" type="text">
					  </p>
					  
					  <p>
						<label for="zipcodeid">Zipcode ID</label>

						<input id="zipcodeid" name="zipcodeid" value="" title="zipcodeid" tabindex="5" type="text">
					  </p>
					  
					  
					  <p class="remember">
						<input id="empaccount" value="Create Employee" tabindex="6" type="button" onclick="loadXMLDoc(this)">
					  </p>"""



        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute("select zipcode_id,city_name,state_name,zipcode from city,state,zipcode where zipcode.city_id=city.city_id and city.state_id=state.state_id order by zipcode_id asc")
        data=c.fetchall()
        db.close()
        i=0

        print """<table border="1"><tr><th>ZIPCODE ID</th><th>CITY</th><th>STATE</th><th>ZIPCODE</th></tr>""" 

        while i<len(data):
        
            


            print """<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"""%(data[i][0],data[i][1],data[i][2],data[i][3])

            i=i+1


        print "</table>"
        print """				</form>
				  </fieldset>
				</div>
				 
				<p class="flip"><button id="1" type="button" onclick="flipper()">Expand/Contract Tool Bar</p>
				 
				</body>
				</html>
				"""
        
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
	print "Content-Type: text/html\n"
   
run()



