import cgi

def run():
    try:
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
					  <input id="cust_id" name="cust_id" value="" title="cust_id" type="text">
					  <input id="custid_submit" value="Search Customer by Id" tabindex="6" type="submit">
					  </p>
					  <label for="username">Username</label>
					  <input id="username" name="username" value="" title="username" type="text">

					  </p>
					  <p>
						<label for="password">Password</label>

						<input id="password" name="password" value="" title="password" tabindex="5" type="password">
					  </p>
					  
					  <p>
						<label for="firstname">FirstName</label>

						<input id="firstname" name="firstname" value="" title="firstname" tabindex="5" type="firstname">
					  </p>
					  
					  <p>
						<label for="lastname">LastName</label>

						<input id="lastname" name="lastname" value="" title="lastname" tabindex="5" type="lastname">
					  </p>
					  
					  <p>
						<label for="phonenum">Phone Num</label>

						<input id="phonenum" name="phonenum" value="" title="phonenum" tabindex="5" type="phonenum">
					  </p>
					  
					  <p>
						<label for="billadd">Billing Addr</label>

						<input id="billadd" name="billadd" value="" title="billadd" tabindex="5" type="billadd">
					  </p>
					  
					  <p>
						<label for="shipadd">Shipping Addr</label>

						<input id="shipadd" name="shipadd" value="" title="shipadd" tabindex="5" type="shipadd">
					  </p>
					  
					  <p>
						<label for="field">Credit Card #</label>
						
						<input class="left" id="field" name="field" >
					  </p>
					  
					  <p class="remember">
						<input id="signin_submit" value="Update" tabindex="6" type="submit">
					  </p>


					</form>
				  </fieldset>
				</div>
				 
				<p class="flip"><button id="1" type="button" onclick="loadXMLDoc(this)" >Update User Info</p>
				 
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



