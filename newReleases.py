import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def query2():


    #print """Content-Type: text/html """

    #print ""



          


    query="""select movie_id,title,year_release,description,photo,trailer_link from movie where is_rented=0 order by year_release desc limit 3"""


    if query!=None:
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()

        i=0

        
        if len(data)==0:
            print "NO RESULTS HAVE BEEN FOUND"

        else:    
            
            print """<table id='table' border="1" align="right">
            <tr><th>Movie ID</th><th>Title</th><th>Date of Release</th><th>Description</th>
            <th>Photo</th><th>View Trailer</th><th>RENT ME</th></tr>"""

            

            while i<len(data):

                #urllib.urlopen('http://localhost//videostore//htdocs//img//temp.jpg',data[i][3]).

                path=os.path.abspath('.'+os.curdir)+"\\htdocs\\img\\%s.jpg"%data[i][1]

                fil=open(path,'wb')

                fil.write(data[i][4])

                fil.close()

               
                
                print """
                
                <tr><td>%s</td><td>%s</td><td>%s</td>
                <td>%s</td><td><img src="/htdocs/img/%s.jpg" width=100 height=100></td>
                <td><a href="%s">Click To View Trailer</a></td>
                <td><input name="%s" id="%s" type="checkbox"></td>    
                   

                </tr>"""%(data[i][0],data[i][1],data[i][2],data[i][3],data[i][1],data[i][5],i,i)

                
                
                
                i=i+1
                
            print """</table>"""

            
           
            

            print """

                    <br/><br/>"""

              
            
            
            db.close()


def basic():

    print """Content-Type: text/html """

    print

    print """

    <html>
    <head>
    
    </head>
    <body><center>"""

    query2()


    print """</center></body>
    </html>
    """



print """Content-Type: text/html """

print
query2()

