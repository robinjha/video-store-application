def home():
    try:
	http_headers() 
        print """
        <html>

        <head>
          <link rel="stylesheet" href="/htdocs/others/mystyle.css">
        </head>

        <body>
	</body>
	</html>"""
         
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
	print "Content-Type: text/html\n"
   
home()


