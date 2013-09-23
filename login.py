import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def login():
    try:
        http_headers()
        
        
	
        print """
        <html>
        <head>
        <link rel="stylesheet" href="/htdocs/others/mystyle.css">
        <title>Login Screen </title>"""

        atts=cgi.FieldStorage()
        username=atts.getvalue('username')
        password=atts.getvalue('password')
        login_employee=0
        login_customer=0

        if username!=None and password!=None:



            db = MySQLdb.connect("localhost","root","pass1","assign3")
            c = db.cursor()
            c.execute("select * from creditcard where username='%s' and password='%s'"%(username,password))
            data=c.fetchall()

            if len(data)>0:
                login_customer=1

            else:
                c.execute("select * from employee where email='%s' and password='%s'"%(username,password))
                data=c.fetchall()
    
                if len(data)>0:
                    login_employee=1

            db.close()
            
            if login_customer==1:
                print """<script type="text/javascript">alert('You have been logged in as customer');
                          document.write('Logged in as: %s');

                          document.cookie = "cooks=" + escape("c"+"%s");

                          
                          document.write('<a href="login.py" onclick="destroyCookie()"> Sign Out</a>');  

                          function destroyCookie(){

                            var cookie_date =new Date();  // current date & time
                            cookie_date.setTime(cookie_date.getTime()-1);
                            document.cookie = "cooks" + "=; expires=" + cookie_date.toGMTString();

                          }

                            
                          </script>"""%(data[0][4],data[0][4])
            elif login_employee==1:
                print """<script type="text/javascript">alert('You have been logged in as employee');
                          document.write('Logged in as: %s');
                          
                          document.cookie = "cooks=" + escape("e"+"%s");

                          
                          document.write('<a href="login.py" onclick="destroyCookie()"> Sign Out</a>');  

                          function destroyCookie(){

                            var cookie_date =new Date();  // current date & time
                            cookie_date.setTime(cookie_date.getTime()-1);
                            document.cookie = "cooks" + "=; expires=" + cookie_date.toGMTString();

                          }
  


                          </script>"""%(data[0][6],data[0][6])
            else:
                print """<script type="text/javascript">alert('Cannot log you in!!!')</script>"""
        

        
        print """
        </head>
        <body>

                
        <form action="login.py" method="post">
        <br>
        <center>
        Username: <input type="text" name="username" style="background:#bfbfbf;color:#212121;border-color:#212121;" onFocus="this.style.background = '#ffffff';" onBlur="this.style.background = #bfbfbf;">
        <br>
        Password: <input type="password" name="password" style="background:#bfbfbf;color:#212121;border-color:#212121;" onFocus="this.style.background = '#ffffff';" onBlur="this.style.background = '#bfbfbf';">
        <br>
        <input type="submit" value="Login" onClick="Login(this.form);" style="background:#bfbfbf;color:#000000;border-color:#212121;" onMouseOver="this.style.color = '#404040';" onMouseOut="this.style.color = '#000000';" onFocusr="this.style.color = '#404040';" onBlur="this.style.color = '#000000';">
        <br><a href="createAccount.py" >Are you a new User?</a>

        </center>
        </form>
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
   
login()
