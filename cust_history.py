import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def query1():
    field=cgi.FieldStorage()
    category=field.getvalue('cust_id','null')
    query=None

    query="""select cust_id,rentals.movie_id,title,photo,date_issued,due_date,date_returned,(curdate()-due_date)*tax.late_fee,(curdate()-due_date) from rentals,movie,tax where (rentals.movie_id=movie.movie_id and cust_id=%s) order by date_issued desc"""%category
    

    if query!=None:
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()

        i=0

        if len(data)==0:
            print "NO RESULTS HAVE BEEN FOUND"

        else:

            print """THE RENTING HISTORY OF CUSTOMER %s is"""%category

            print """<table id='return_table' border="1">
            <tr><th>Customer ID</th><th>Movie ID</th><th>Title</th><th>Photo</th>
            <th>Date Issued</th><th>Date Due</th><th>Date Returned</th><th>Late Fee</th><th>Days Late</th></tr>"""

            

            while i<len(data):

                #urllib.urlopen('http://localhost//videostore//htdocs//img//temp.jpg',data[i][3]).

                path=os.path.abspath('.'+os.curdir)+"\\htdocs\\img\\%s.jpg"%data[i][2]

                fil=open(path,'wb')

                fil.write(data[i][3])

                fil.close()


                if data[i][7]<=0:

                    print """
                    
                    <tr><td>%s</td><td>%s</td><td>%s</td>
                    <td><img src="/htdocs/img/%s.jpg" width=100 height=100></td>
                    <td>%s</td><td>%s</td><td>%s</td><td bgcolor="#FF0000">0</td><td>0</td>    
                       

                    </tr>"""%(data[i][0],data[i][1],data[i][2],data[i][2],data[i][4],data[i][5],data[i][6])

                else:

                    print """
                    
                    <tr><td>%s</td><td>%s</td><td>%s</td>
                    <td><img src="/htdocs/img/%s.jpg" width=100 height=100></td>
                    <td>%s</td><td>%s</td><td>%s</td><td bgcolor="#FF0000">%s</td><td>%s</td>    
                       

                    </tr>"""%(data[i][0],data[i][1],data[i][2],data[i][2],data[i][4],data[i][5],data[i][6],data[i][7],data[i][8])

                   
                
                
                i=i+1
                
            print """</table>"""

            

            print """

                    <br/><br/>
                
                """    
            
            
            db.close()


def searchPage():

    print "Content-type: text/html"
    print

    query1()

searchPage()
