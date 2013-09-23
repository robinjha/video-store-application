#!/usr/bin/env python

#!/usr/bin/python



def run():
    try:
        html = []
        
        html += ["""
        <html>

        <head>
          <title> the Movie DB </title>
          <link rel="stylesheet" href="/htdocs/others/mystyle.css">
        </head>

        <ul class="navbar">
          <li><a href="/others/index.html" target = "Frame_body" >HOME PAGE</a>
          <li><a href="newreleases.py" target = "Frame_body">NEW RELEASES</a>
          <li><a href="assign3_q5.py" target = "Frame_body">NEW Additions</a>
        <li><a href="mostpopular.html" target = "Frame_body">MOST POPULAR</a>
          <li><a href="genre.py" target = "Frame_body">SEARCH BY GENRE</a>
          <li><a href="account.py" target="Frame_body">MY ACCOUNT</a>
          <li><a href="login.py" target="Frame_body">LOGIN</a>
        </ul>

        </html>
        """]
        
        html += [""]
        http_headers()
        print '\n'.join(html)
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
    print "Content-Type: text/html\n"
    
run()
