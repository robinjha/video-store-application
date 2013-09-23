#!/usr/bin/env python

def pastDue():
    try:
        http_headers()
        print '''
                 <html>
                 <body>
                 <h2>Overdue Items</h2>
                 
                 
                 </body>
                 </html>
                 '''  
    except:
        http_headers()
        print "<!-- --> <hr><h1>Oops... an error occurred.</h1>"
        cgi.print_exception()

def http_headers():
    print "Content-Type: text/html\n"
    
pastDue()
