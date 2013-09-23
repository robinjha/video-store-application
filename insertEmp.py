import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib


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
    address=atts.getvalue('address')
    zipcodeid=atts.getvalue('zipcodeid')
    

    query="""select email from employee where email like '%s'"""%username
    db = MySQLdb.connect("localhost","root","pass1","assign3")
    c = db.cursor()
    c.execute(query)
    data=c.fetchall()

    message=""


    if len(data)>0 or username==None or password==None or firstname==None or lastname==None or phonenum==None or address==None or zipcodeid==None:
        message="Fields missing or username already exists please restart whole registration process"

         
        
    else:

        
        query="""insert into employee (first_name,last_name,password,address,phone_number,email,zipcode_id) values ('%s','%s','%s','%s','%s','%s',%s)"""%(firstname,lastname,password,address,phonenum,username,zipcodeid)
        c.execute(query)
        db.commit()

        db.close()

        message="Thank you for registering as an employee"
        
    print "</head><body>%s</body></html>"%message


main()
