import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def query1():
    
    query="""select customer.cust_id,first_name,last_name,billing_address,shipping_address,rentals.movie_id,title,photo,date_issued,due_date,total_cost,curdate()-due_date,(curdate()-due_date)*2 from movie,rentals,customer,creditcard where (customer.cust_id=rentals.cust_id and rentals.movie_id=movie.movie_id and customer.cust_id=creditcard.cust_id and curdate()>due_date)"""
    

    if query!=None:
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()

        i=0

        if len(data)==0:
            print "NO RESULTS HAVE BEEN FOUND"

        else:


            print "<h1>MOVIES OVERDUE</h1>\n"
            
            print """<table id='table' border="1">
            <tr><th>Customer ID</th><th>First Name</th><th>Last Name</th><th>Billing Address</th>
            <th>Shipping Address</th><th>Movie ID</th><th>Title</th><th>Photo</th><th>Date Issued</th><th>Due Date</th><th>Rent</th><th>Days Overdue</th><th>Late Fees</th></tr>"""

            

            while i<len(data):

                #urllib.urlopen('http://localhost//videostore//htdocs//img//temp.jpg',data[i][3]).

                path=os.path.abspath('.'+os.curdir)+"\\htdocs\\img\\%s.jpg"%data[i][6]

                fil=open(path,'wb')

                fil.write(data[i][7])

                fil.close()


                

                print """
                    
                    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                    <td><img src="/htdocs/img/%s.jpg" width=100 height=100></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                        
                       

                    </tr>"""%(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][6],data[i][8],data[i][9],data[i][10],data[i][11],data[i][12])

                
                   
                
                
                i=i+1
                
            print """</table>"""

            

            
            
            db.close()


def searchPage():

    print "Content-type: text/html"
    print

    query1()

searchPage()
