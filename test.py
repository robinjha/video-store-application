#!C:\Python27\python.exe -u 

import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
from PIL import Image
from StringIO import StringIO
import sys
import urllib


def searchPage():



    print "Content-Type: text/html\n"

    print """

    

    <html><head><title>Test</title></head>

    <body>

    hello world

    <img src='/htdocs/img/Koala.jpg' >

    </body>
    </html>


    """

searchPage()
