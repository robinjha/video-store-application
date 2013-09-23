import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib
import Cookie


def transaction():

    try:
    
    
    
        field=cgi.FieldStorage()
        val=field.getvalue("reserved")

        val=val.split("_")

        cookie=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])

        s=cookie["cooks"].value

        s=s[1:]

        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()


        query="select * from tax"
        c.execute(query)
        data=c.fetchall()

        e_tax=data[0][0]/100;
        s_tax=data[0][1]/100;
        tax=(e_tax+s_tax)+1;
        
        query="""select cust_id from creditcard where username='%s'"""%s
        
        c.execute(query)
        data=c.fetchall()

        cust_id=data[0][0]

        for i in val:
            
            query='''select price from movie as m,pricegroup as p where m.pricegroup_id = p.pricegroup_id and m.movie_id = %s '''%i
            c.execute(query)
            data=c.fetchall()
            db.close()
            db = MySQLdb.connect("localhost","root","pass1","assign3")
            c = db.cursor()
            price=int(data[0][0])
            query='''select curdate(),adddate(curdate(),14)'''
            c.execute(query)
            data=c.fetchall()
            query='''insert into rentals (cust_id,movie_id,total_cost,date_issued,due_date,date_returned,on_time) values(%s,%s,%s,'%s','%s',null,'0')'''%(cust_id,i,price*tax,data[0][0],data[0][1])
            c.execute(query)
            db.commit()
            query='''update movie set is_rented='%s' where movie_id=%s'''%(1,i)
            c.execute(query)
            db.commit()

        db.close()

    except:

        print "Content-type: text/html"

        print

        print """

        <html>
        <head>

        ALL MOVIES YOU SELECTED ARE RENTED OUT

        </head>

        <body>
        
        </body>

        </html>
        """
        



transaction()

