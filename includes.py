from includes import *
import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib


def query1():
    field=cgi.FieldStorage()
    form=field.getvalue('Query','null')
    category=field.getvalue('category','null')
    query=None

    string=form.split()
    string_set=''

    for i in string:
        string_set=string_set+"'%s' "%(i)

    form=','.join(string_set.split())

    

    if category=="movie":
        query="""select title,year_release,description,photo,trailer_link from movie where title in (%s)"""%form
    elif category=="actor":
        query="""select distinct title,year_release,description,photo,trailer_link from cast,castmovie,movie where movie.movie_id=castmovie.movie_id and castmovie.cast_id=cast.cast_id and (cast.first_name in (%s) or cast.last_name in (%s))"""%(form,form)
    elif category=="director":
        query="""select title,year_release,description,photo,trailer_link from director,castmovie,movie where movie.movie_id=castmovie.movie_id and castmovie.director_id=director.director_id and (director.first_name in (%s) or director.last_name in (%s))"""%(form,form)


    if query!=None:
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()

        i=0

        print """<table border="1"><tr><th>Title</th><th>Date of Release</th><th>Description</th>
        <th>Photo</th><th>Trailer Links</th></tr>"""

        while i<len(data):

            #urllib.urlopen('http://localhost//videostore//htdocs//img//temp.jpg',data[i][3]).

            path="C:\\Project\\htdocs\\img\\%s.jpg"%data[i][0]

            fil=open(path,'wb')

            fil.write(data[i][3])

            fil.close()

           
            
            print """<tr><td>%s</td><td>%s</td><td>%s<button title='READ MORE'/></td><td><img src="/htdocs/img/%s.jpg" width=100 height=100></td><td><a href='%s' target='_blank'>View Trailer</a></td></tr>"""%(data[i][0],data[i][1],data[i][2],data[i][0],data[i][4])

            i=i+1
            
        print """</table>"""

        db.close()

def includes():
    try:
        html = []
	http_headers()
	
        html += ["""
        <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
        <html>

        <head>
          <title> the Movie DB </title>
          <link rel="stylesheet" href="/htdocs/others/mystyle.css">
        </head>

        <body>
        
        <!-- Site navigation menu -->
        <ul class="navbar">
          <li><a href="/htdocs/others/index.html">HOME PAGE</a>
          <li><a href="newReleases.py">NEW RELEASES</a>
          <li><a href="newAdditions.py">NEW ADDITIONS</a>
          <li><a href="searchByGenre.py">SEARCH MOVIES BY GENRE</a>
          <li><a href="/htdocs/others/town.html">MOST POPULAR</a>
          <li><a href="/htdocs/others/links.html">LINKS</a>
        </ul>"""]

        print '\n'.join(html)

        
        query1()        

        html=["""<!--table for the search box-->
        <table width="150" align="right">
                <td>
                        <a href="login.py"><i>Login</i></a>
                </td>
                <td>
                <tr>
                        <td colspan = "2"></td>
                </tr>
                       
                        <td>
                        </td>
                        <td>
                                <form action="includes.py" method="post">
                                <input type="submit" name="Search" value="Search">
                                

                                <input type ="text" name="Query" size="15"/>
                                <select name="category">
                                <option value="movie">Movie</option>
                                <option value="actor">Actor</option>
                                <option value="director">Director</option>
                                </select>
                                <br>
                                 </form>
                        </td>
                        
                        </tr>
                        </td>
        </table>
        
        </body>
        </html>
        """]
        print '\n'.join(html)
        
        html += [""]
        #http_headers()
        #print '\n'.join(html)
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
	print "Content-Type: text/html\n"
   

includes()
