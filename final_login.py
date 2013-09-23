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
			
			<title>Janet's Video Store</title>
		<style type="text/css"> 

		#navbar ul { 
				margin: 0; 
				padding: 5px; 
				list-style-type: none; 
				text-align: center; 
				background-color: #000; 
				} 
		 
		#navbar ul li {  
				display: inline; 
				} 
		 
		#navbar ul li a { 
				text-decoration: none; 
				padding: .2em 1em; 
				color: #fff; 
				background-color: #000; 
				} 
		 
		#navbar ul li a:hover { 
				color: #000; 
				background-color: #fff; 
				} 
		 
		</style>""" 
                        

        atts=cgi.FieldStorage()
        username=atts.getvalue('username')
        password=atts.getvalue('password')
        login_employee=0
        login_customer=0

        if username!=None and password!=None:



            db = MySQLdb.connect("localhost","root","pass1","assign3")
            c = db.cursor()
            c.execute("select * from creditcard where username like '%s' and password like '%s'"%(username,password))
            data=c.fetchall()

            if len(data)>0:
                login_customer=1

            else:
                c.execute("select * from employee where email like '%s' and password like '%s'"%(username,password))
                data=c.fetchall()
    
                if len(data)>0:
                    login_employee=1

            db.close()
            
            if login_customer==1:
                print """<script type="text/javascript">alert('You have been logged in as customer');
                          

                          document.cookie = "cooks=" + escape("c"+"%s");

                           window.location.replace("navbar_ver1.py?cust_id=%s");
                          
                          

                          function destroyCookie(){

                            var cookie_date =new Date();  // current date & time
                            cookie_date.setTime(cookie_date.getTime()-1);
                            document.cookie = "cooks" + "=; expires=" + cookie_date.toGMTString();

                          }

                            
                          </script>"""%(data[0][4],data[0][1])
            elif login_employee==1:
                print """<script type="text/javascript">alert('You have been logged in as employee');
                          
                          
                          document.cookie = "cooks=" + escape("e"+"%s");

                          window.location.replace("emp_leftframe.py");  
                          
                            

                          function destroyCookie(){

                            var cookie_date =new Date();  // current date & time
                            cookie_date.setTime(cookie_date.getTime()-1);
                            document.cookie = "cooks" + "=; expires=" + cookie_date.toGMTString();

                          }
  


                          </script>"""%(data[0][6])
            else:
                print """<script type="text/javascript">alert('Cannot log you in!!!')</script>"""    





        print        	"""<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
			<script src="http://code.jquery.com/jquery-latest.js"></script>
			<script type="text/javascript" src="http://dev.jquery.com/view/trunk/plugins/validate/lib/jquery.delegate.js"></script>
			<script type="text/javascript" src="http://dev.jquery.com/view/trunk/plugins/validate/jquery.validate.js"></script>
			<script type="text/javascript">
			jQuery.validator.setDefaults({
				debug: true,
				success: "valid"
			});;
			</script>

			  <script>
			  $(document).ready(function(){
				$("#signin").validate({
			  rules: {
				field: {
				  required: true,
				  creditcard: true
				}
			  }
			});
			  });
			  </script>
			  
			<script type="text/javascript"> 
			$(document).ready(function(){
			$(".flip1").click(function(){
				$(".panel1").slideToggle("slow");
			  });
			});
			</script>
			
			
			<script type="text/javascript"> 
			$(document).ready(function(){
			$(".flip2").click(function(){
				$(".panel2").slideToggle("slow");
			  });
			});


                        function test(){


                            

                                window.location.replace('enter_info.py?username='+document.getElementById('username').value+"&password="+document.getElementById('password').value+"&firstname="+document.getElementById('firstname').value+"&lastname="+document.getElementById('lastname').value+"&phonenum="+document.getElementById('phonenum').value+"&billadd="+document.getElementById('billadd').value+"&shipadd="+document.getElementById('shipadd').value+"&billzipid="+document.getElementById('billzipid').value+"&field="+document.getElementById('field').value);

                        }





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
			height:450px;
			display:none;
			}
			
			</style>
			</head>
			 
			<body>
			
			
			<div id="navbar"> 
			<ul> 
			<li><p class="flip2"><button id="2" type="button" onclick="loadXMLDoc(this)">Login</p></li>
			<li><p class="flip1"><button id="1" type="button" onclick="loadXMLDoc(this)">New User</p></li>
	       </ul> 
			</div>
		
			<div class="panel1">
			
			<fieldset id="signin_menu">
					<form method="post" action="enter_info.py" id="login">
					  <p>
					  <label for="username">Username</label>
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
					  """

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


        print                            """</table><p>
						<label for="billadd">Billing Addr</label>

						<input id="billadd" name="billadd" value="" title="billadd" tabindex="5" type="text">
					  </p>

					   
					  
					  <p>
						<label for="shipadd">Shipping Addr</label>

						<input id="shipadd" name="shipadd" value="" title="shipadd" tabindex="5" type="text">
					  </p>

					   <p>
						<label for=billzipid"">Zipcode ID</label>

						<input id="billzipid" name="billzipid" value="" title="billzipid" tabindex="5" type="text">
					  </p>

					  
					  <p>
						<label for="field">Credit Card #</label>
						
						<input class="left" id="field" type="text" name="field">
					  </p>
					  
					  <p class="remember">
						<input type="submit" id="signin_submit" value="Create User" tabindex="6">
					  </p>

					</form>
				  </fieldset>
				</div>
				
				 
				
				
			<div class="panel2">
			<fieldset id="login_menu">
								<form method="post" action="final_login.py" id="login">
								  <label for="username">Username</label>
								  <input id="username" name="username" value="" title="username" type="text">

								  </p>
								  <p>
									<label for="password">Password</label>

									<input id="password" name="password" value="" title="password" tabindex="5" type="password">
								  </p>
								  <p class="remember">
									<input type="submit" id="signin_submit" value="Sign in" tabindex="6">
								  </p>

								</form>
							  </fieldset>
			</div>
			
			<h1 align="center">Janet's Video Store--Login Page</h1>
			<table align="center">
			<tr>
			<td><img src=/htdocs/others/thumb1.jpg></td>
			<td><img src=/htdocs/others/thumb2.jpg></td>
			<td><img src=/htdocs/others/thumb3.jpg></td>
			</tr>
			</table>
				
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



