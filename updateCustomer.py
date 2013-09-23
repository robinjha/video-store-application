#!/usr/bin/env python
import cgi
def updateCustomer():
    try:
        html = []
        
        html += ['''
                <html>
                <body>
                Do you want to create or update a customer's account?
                 
                <form name="input" action="updateCustomer.py" method="post">
                <input type="radio" name="change" value="create" /> Create<br />
                <input type="radio" name="change" value="update" /> Update<br />
                <input type="submit" value="Submit" />
                </form> 
                </body>
                ''']
        form = cgi.FieldStorage()

        if form.has_key("change"):
            if form["change"].value == "create":
                html += ["This will go to the Create Page (we already made this)"]
            else:
                html += ['''This will update the account
                         <form name="input" action="updateCustomer.py" method="post">
                         Customer ID: <input type = "text" name = "custID" />
                         <input type="submit" value="Submit" />
                         </form>
                         ''']
        
        if form.has_key("custID"):
            html += ["Bring up customer's info (Go to database)"]
            

        http_headers()
        print "\n".join(html)    
    except:
        http_headers()
        print "<!-- --> <hr><h1>Oops... an error occurred.</h1>"
        cgi.print_exception()

def http_headers():
    print "Content-Type: text/html\n"
    
updateCustomer()