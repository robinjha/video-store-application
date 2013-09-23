import cgi
import cgitb;cgitb.enable()


def run():
    try:
        html = []
        

        http_headers()

        print """
        <html>

        <head>
                <link rel="stylesheet" href="/htdocs/others/mystyle.css">
                <script type="text/javascript">

                function checkCookie(){

                    var results = document.cookie.match( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

                              if(results){
                                
                                document.getElementById('link1').innerHTML="LOG OUT"}
                }

                
		
                function changeSrc()
                {


                    
                   parent.document.getElementById('Frame_body').src = "assign3_start.py"
            
                }
		</script>
        </head>
        <body>
       
        <table width="150" align="right">

	<tr><a href="login.py" name="link1" onclick="checkCookie()"><i>Login</i></a></tr>
	
	<tr>	
                <form name="query" action="assign3_start.py" method="post" onsubmit="changeSrc()" target="Frame_body">
		<td><input type ="text" name="Query" size="15"/></td>
		<td><input type="submit" id="Search" value="Search" ></td>
                

        </tr>
        
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <tr>
                <select style="WIDTH: 89px" size=1 name="search">
      		<option value="movie">Movie</option>
      		<option value="actor">Actor</option> 
      		<option value="director">Director</option> &lt;\SELECT&gt;</select>
            </form>

        </tr>
        </table>
        </body>
        </html>
        """
        
        #print '\n'.join(html)
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
    print "Content-Type: text/html\n"
    
run()
