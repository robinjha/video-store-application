#!/usr/bin/env python
import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib

def query1():


    query="""select movie_id,title,year_release,description,photo from movie order by arrival_date desc limit 6"""


    if query!=None:
        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
        c.execute(query)
        data=c.fetchall()

        i=0

        print """<form method="get"  action="renting.py">"""

        print """<table id='table' border="1">
        <tr><th>Movie ID</th><th>Title</th><th>Date of Release</th><th>Description</th>
        <th>Photo</th><th>View Trailer</th><th>RENT ME</th></tr>"""

        while i<len(data):

            #urllib.urlopen('http://localhost//videostore//htdocs//img//temp.jpg',data[i][3]).

            path=os.path.abspath('.'+os.curdir)+"\\htdocs\\img\\%s.jpg"%data[i][0]

            fil=open(path,'wb')

            fil.write(data[i][4])

            fil.close()

           
            
            print """
            
            <tr><td>%s</td><td>%s</td><td>%s</td>
            <td>%s<input type="button" value="READ MORE" /></td>
            <td><img src="/htdocs/img/%s.jpg" width=100 height=100></td>
            <td><a href="%s">Click To View Trailer</a></td>
            <td><input name="%s" id="%s" type="checkbox"> </td>    
               

            </tr>"""%(data[i][0],data[i][1],data[i][2],data[i][3],data[i][1],data[i][5],i,i)

            i=i+1
            
        print """</table>"""


        print """<script type="text/javascript">




        function getData(){

        	
        var pass="reserved=";
        for(i=1;i<=%s;i++){
        var x=document.getElementById('table').rows[i].cells;
        z=document.getElementById(""+(i-1));
        if(z.checked){
        pass+=x[0].innerHTML+"_";}
        }

        var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

        if(results){
        window.location="renting.py?"+pass;}
        else
        alert('you have to log-in')
       
        
        

        }
        </script> """%len(data)


        print """

                <br/><br/>
                
                <input type="button" value='Check Out' onclick="getData()"/>

            </form> 
            """    
        
        
        db.close()




def basic():

    print """Content-Type: text/html """

    print

    print """

    <html>
    <head>
    <link rel="stylesheet" href="/htdocs/others/mystyle.css">
    </head>
    <body><center>"""

    query2()


    print """</center></body>
    </html>
    """

basic()



