import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib
import MySQLdb

def main():

    d=0


    print "Content-type: text/html"

    print 


    print """<html><head>"""





    atts=cgi.FieldStorage()

    password=atts.getvalue('password')
    firstname=atts.getvalue('firstname')
    lastname=atts.getvalue('lastname')
    phonenum=atts.getvalue('phonenum')
    bill_addr=atts.getvalue('bill_addr')
    ship_addr=atts.getvalue('ship_addr')
    ccn=atts.getvalue('ccn')
    cust_id=atts.getvalue('cust_id')



    

    if cust_id!=None:

        d=1

        print ccn

        db = MySQLdb.connect("localhost","root","pass1","assign3")
        c = db.cursor()

        c.execute("""update customer set first_name='%s',last_name='%s' where cust_id=%s"""%(firstname,lastname,cust_id))
        db.commit()

        c.execute("""update phone set phone_num='%s' where cust_id=%s"""%(phonenum,cust_id))
        db.commit()

        c.execute("""update creditcard set ccn='%s',billing_address='%s',shipping_address='%s',password='%s' where cust_id=%s"""%(ccn,bill_addr,ship_addr,password,cust_id))
        db.commit()

        db.close()
        
    if d==1:
        print """</head><body>Your Account has Been Successfully Updated Thankyou!!!!!!!!!</body></html>"""

    else:
        print """</head><body>Your Account has not Been Successfully Updated Thankyou!!!!!!!!!</body></html>"""


main()
