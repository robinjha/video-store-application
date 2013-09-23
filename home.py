from includes import *
import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def home():
    try:
        html = []
	    
        includes()
               
        #print '\n'.join(html)
        
        html += [""]
        http_headers()
        
        print '\n'.join(html)
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        #cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
	print "Content-Type: text/html\n"
   
home()
