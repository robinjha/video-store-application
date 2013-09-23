#!/usr/bin/env python
import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def query1():
    field=cgi.FieldStorage()
    category=field.getvalue('choice','null')
    query=None

    query="""select title,year_release,description,photo from movie,genre where movie.genre_id=genre.genre_id and type like '%s'"""%category
    

    if query!=None and category!='null':
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()

        i=0

        print """<table border="1"><tr><th>Title</th><th>Date of Release</th><th>Description</th>
        <th>Photo</th></tr>"""

        while i<len(data):

            #urllib.urlopen('http://localhost//videostore//htdocs//img//temp.jpg',data[i][3]).

            path=os.curdir+"\\img\\%s.jpg"%data[i][0]

            fil=open(path,'wb')

            fil.write(data[i][3])

            fil.close()

           
            
            print """<tr><td>%s</td><td>%s</td><td>%s<button title='READ MORE'/></td><td><img src="/cgi-bin/img/%s.jpg" width=100 height=100></td></tr>"""%(data[i][0],data[i][1],data[i][2],data[i][0])

            i=i+1
            
        print """</table>"""

        db.close()





def searchPage():

    print "Content-type: text/html"
    print

    print """
            <html>

            <head><title>Search For Movie</title></head>

            <body>"""

    query1()

    print """

            <form method="post" action="assign3_q7.py">
                
               <p> <select name="choice">
                    <option value="action">action</option>
                    <option value="adventure">adventure</option>
                    <option value="drama">drama</option>
                    <option value="documentary">documentary</option>
                    <input type="submit" value="LOOK UP FOR MOVIE" />
                </select></p>    
            
            </form>

            
    </body>
            </html>
            """



searchPage()
