import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib
import Cookie


def transaction():

    try:
    
    
    
        field=cgi.FieldStorage()

        val1=field.getvalue("cust_id")
        val=field.getvalue("reserved")

        val=val.split("_")

        
        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()
                
        
        
       
        cust_id=val1;

        for i in val:
            
            query="""select curdate()-due_date from rentals where cust_id=%s and movie_id=%s and date_returned is null"""%(cust_id,i)

            c.execute(query)

            data=c.fetchall()

            days=data[0][0]

            if days>0:

                c.execute("""update rentals set date_returned=curdate(),total_cost=total_cost+%s where movie_id=%s and cust_id=%s"""%(days*2,i,cust_id))
                
                db.commit()

                c.execute("""update movie set is_rented=0 where movie_id=%s"""%i)
                
                db.commit()

            else:

                c.execute("""update rentals set date_returned=curdate() where movie_id=%s and cust_id=%s"""%(i,cust_id))
                
                db.commit()

                c.execute("""update movie set is_rented=0 where movie_id=%s"""%i)
                
                db.commit()





        db.close()

    except:

        print "Content-type: text/html"

        print

        print """

        <html>
        <head></head>

        <body>
        All MOVIES YOU SELECTED ARE RETURNED
        </body>

        </html>
        """
        



transaction()

