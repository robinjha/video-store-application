import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib



def run():
    try:

        info=cgi.FieldStorage()
        cust_id=info.getvalue('cust_id')

        query="""select first_name,last_name from customer where cust_id=%s"""%cust_id
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()
        firstname=data[0][0]
        lastname=data[0][1]


        query="""select phone_num from phone where cust_id=%s"""%cust_id
        c.execute(query)
        data=c.fetchall()
        phonenum=data[0][0]


        query="""select * from creditcard where cust_id=%s"""%cust_id
        c.execute(query)
        data=c.fetchall()
        
        ccn=data[0][0]
        bill_addr=data[0][2]
        ship_addr=data[0][3]
        username=data[0][4]
        password=data[0][5]










        http_headers()
        print """
			<html>
			<head>
			<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
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
			height:400px;
			display:none;
			}
			
			</style>
			</head>
			 
			<body>
			 
			<div class="panel">
			<fieldset id="signin_menu">
					<form method="post" id="signin">
					  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
					  <label for="cust_id">Customer Id</label>
					  <input id="cust_id" name="cust_id" value="%s" title="cust_id" type="text" readonly="readonly">
					
					  </p>
					  <label for="username">Username</label>
					  <input id="username" name="username" value="%s" title="username" type="text" readonly="readonly">

					  </p>
					  <p>
						<label for="password">Password</label>

						<input id="password" name="password" value="%s" title="password" tabindex="5" type="password">
					  </p>
					  
					  <p>
						<label for="firstname">FirstName</label>

						<input id="firstname" name="firstname" value="%s" title="firstname" tabindex="5" type="firstname">
					  </p>
					  
					  <p>
						<label for="lastname">LastName</label>

						<input id="lastname" name="lastname" value="%s" title="lastname" tabindex="5" type="lastname">
					  </p>
					  
					  <p>
						<label for="phonenum">Phone Num</label>

						<input id="phonenum" name="phonenum" value="%s" title="phonenum" tabindex="5" type="phonenum">
					  </p>
					  
					  <p>
						<label for="billadd">Billing Addr</label>

						<input id="billadd" name="billadd" value="%s" title="billadd" tabindex="5" type="billadd">
					  </p>
					  
					  <p>
						<label for="shipadd">Shipping Addr</label>

						<input id="shipadd" name="shipadd" value="%s" title="shipadd" tabindex="5" type="shipadd">
					  </p>
					  
					  <p>
						<label for="field">Credit Card #</label>
						
						<input class="left" id="field" name="field" value="%s">
					  </p>
					  
					  <p class="remember">
						<input id="signin_submit" value="Update" tabindex="6" type="button" onclick="loadXMLDoc(this)">
					  </p>


					</form>
				  </fieldset>
				</div>
				 
				<p class="flip"><button id="1" type="button" onclick="flipper()">Update User Info</p>
				 
				</body>
				</html>
				"""%(cust_id,username,password,firstname,lastname,phonenum,bill_addr,ship_addr,ccn)
        
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
	print "Content-Type: text/html\n"
   
run()



