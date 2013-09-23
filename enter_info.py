import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib


def is_luhn_valid(cc):
    num = [int(x) for x in str(cc)]    
    return not sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10

def main():

    print "Content-type: text/html"

    print 


    print """<html><head>"""

    atts=cgi.FieldStorage()

    username=atts.getvalue('username')
    password=atts.getvalue('password')
    firstname=atts.getvalue('firstname')
    lastname=atts.getvalue('lastname')
    phonenum=atts.getvalue('phonenum')
    billadd=atts.getvalue('billadd')
    shipadd=atts.getvalue('shipadd')
    billzipid=atts.getvalue('billzipid')
    ccn=atts.getvalue('field')


    query="""select username from creditcard where username='%s'"""%username
    db = MySQLdb.connect("localhost","root","pass1","assign3")
    c = db.cursor()
    c.execute(query)
    data=c.fetchall()

    


    if len(data)>0 or username==None:

        print """<script type="text/javascript">
                alert('Username Exisits Please try a new one');
                window.location.replace("final_login.py");
         </script> """


    elif is_luhn_valid(ccn)==False:

        print """<script type="text/javascript">
                alert('Fake Credit Card Number');
                window.location.replace("final_login.py");
         </script> """


    else:

        query="""select count(*) from customer"""
        c.execute(query)
        data=c.fetchall()


        query="""insert into customer (first_name,last_name,zipcode_id) values ('%s','%s',%s)"""%(firstname,lastname,billzipid)
        c.execute(query)
        db.commit()

        query="""insert into creditcard (ccn,cust_id,billing_address,shipping_address,username,password) values ('%s',%s,'%s','%s','%s','%s')"""%(ccn,data[0][0]+1,billadd,shipadd,username,password)
        c.execute(query)
        db.commit()

        db.close()

        print '''<script type="text/javascript">
                alert("Thank you for joining Janet Video shop");
                
                window.location.replace("navbar_ver1.py");
         </script> '''

        
    print """</head><body><script type="text/javascript">alert("Thank you for joining Janet Video shop")</script></body></html>"""


main()
