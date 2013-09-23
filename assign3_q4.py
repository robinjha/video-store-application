#!/usr/bin/env python
import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def query1():


    query="""select title,year_release,description,photo from movie order by year_release desc limit 3"""


    if query!=None:
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()

        i=0

        print """<table border="1"><tr><th>Title</th><th>Date of Release</th><th>Description</th>
        <th>Photo</th></tr>"""

        while i<len(data):

            #urllib.urlopen('http://localhost//videostore//htdocs//img//temp.jpg',data[i][3]).

            path="C:\\Project\\htdocs\\img\\%s.jpg"%data[i][0]

            fil=open(path,'wb')

            fil.write(data[i][3])

            fil.close()

           
            
            print """<tr><td>%s</td><td>%s</td><td>%s<button title='READ MORE'/></td><td><img src="/htdocs/img/%s.jpg" width=100 height=100></td></tr>"""%(data[i][0],data[i][1],data[i][2],data[i][0])

            i=i+1
            
        print """</table>"""

        db.close()





def searchPage():

    print "Content-type: text/html"
    print

    print """
            <html>

            <head><title>New Releases</title></head>

            <body>"""

    query1()

    print """

            
            
    </body>
            </html>
            """



searchPage()
