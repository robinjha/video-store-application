#!/usr/bin/env python

def createEmployee():
    try:
        html = []
        
        html += ['''
                 <html>
                 <body>
                 <h2>Create Employee</h2>
                 <form name = "input" action = "boo.py" method = "post">
                 User Name: <input type = "text" name = "username" /> <br />
                 Password: <input type = "password" name = "password" /> <br />
                 <br />
                 First Name: <input type = "text" name = "firstname" /> <br />
                 Last Name: <input type = "text" name = "lastname" /> <br />
                 Email Address: <input type = "text" name = "email" /> <br />
                 Address: <input type = "text" name = "address" /> <br />
                 Phone Number: <input type = "text" name = "phone" /> <br />
                 <input type = "submit" value = "Submit" />
                 </input>
                 </form>
                 
                 </body>
                 </html>
                 ''']
        http_headers()
        print "/n".join(html)
    
    except:
        http_headers()
        print "<!-- --> <hr><h1>Oops... an error occurred.</h1>"
        cgi.print_exception()

def http_headers():
    print "Content-Type: text/html\n"
    
createEmployee()
