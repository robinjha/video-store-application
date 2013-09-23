import cgi
from includes import *

#from test import test
#NOTE: IN 4ATTEMPT, DO WE REALLY NEED TEST.PY?


#Class: CreateAccount
#Purpose: Creates a customer user account
    
    #Function: is_luhn_valid
    #Purpose: Uses the luhn algorithm to make sure credit number is accurate
def is_luhn_valid(cc):
    num = [int(x) for x in str(cc)]
    return not sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10    
    
    #Function: run
    #Purpose: The main function that the cgi script calls
def run():
    try:
        html = []
	includes()
        html += ['<form name="input" action="createAccount.py" method="post">',
	        'User Name: <input type="text" name="UserName" align="right" /><br />',
                'Password: <input type="password" name="Password"/><br />',"<br />",
                'First name: <input type="text" name="FirstName"/><br />',
                'Last name: <input type="text" name="LastName"/><br />',
                'Phone Number: <input type="text" name="PhoneNumber"/><br />',
                'Billing Address: <input type="text" name="BillingAddress"/><br />',
                'Shipping Address: <input type="text" name="ShippingAddress"/><br />',
                'Credit Card Number: <input type="text" name="CreditCard"/><br />',
                '<input type="submit" value="Submit" name = "Submit" />',
                '</form> ']
        #print '\n'.join(html)
        form = cgi.FieldStorage()
        if form.has_key("CreditCard"):
            credit_card = form["CreditCard"].value

            try:
                int(credit_card)
                if is_luhn_valid(credit_card):
		    
                    html += ["Your account has been made. You will be redirected to the main page",
			     "or you can click HERE"]
                else:
                    html += ["You entered an invalid credit card number. Click",
			     "<A HREF='javascript:javascript:history.go(-1)'>HERE</A> to try again."]
            except:
                    html += ["Please make sure that the credit card number you entered is an actual number. Click",
			     "<A HREF='javascript:javascript:history.go(-1)'>HERE</A> to try again."]
        else:
            html += [""]
        http_headers()
        print '\n'.join(html)
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
	print "Content-Type: text/html\n"
   
run()
