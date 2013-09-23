import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib


def run():
    try:
        http_headers()

        atts=cgi.FieldStorage()

        cust_id=atts.getvalue('cust_id')
        
        print '''
		
		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
		<html xmlns="http://www.w3.org/1999/xhtml"> 
		<head> 
                
		<title>Janet's Video Store</title>
		<style type="text/css"> 

		#navbar ul { 
				margin: 0; 
				padding: 5px; 
				list-style-type: none; 
				text-align: center; 
				background-color: #000; 
				} 
		 
		#navbar ul li {  
				display: inline; 
				} 
		 
		#navbar ul li a { 
				text-decoration: none; 
				padding: .2em 1em; 
				color: #fff; 
				background-color: #000; 
				} 
		 
		#navbar ul li a:hover { 
				color: #000; 
				background-color: #fff; 
				}

                		
		 
		</style>

		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
	  <script type="text/javascript" src="http://plugins.learningjquery.com/expander/jquery.expander.js"></script>
		<script type="text/javascript"> 
			function flipper(){
			$(".flip").click(function(){
				$(".panel").slideToggle("slow");
			  });
			}
			</script>
	    <script type="text/javascript">

             function testing(obj){
			  
			  $("div.expandable p").expander({
				slicePoint:       40,  // default is 100
				collapseTimer:    15000, // re-collapses after 5 seconds; default is 0, so no re-collapsing
				userCollapseText: '[^]'  // default is '[collapse expanded text]'
			  });

			  obj.onclick=null;
			  
		    
                        }

            function luhn_check(card_number)
{
	
	cc_array = card_number.split( "" )
	cc_array.reverse()
	digit_string = ""
	
	for ( counter=0; counter < cc_array.length; counter++ )
	{
		current_digit = parseInt( cc_array[counter] )
		
		if (counter%%2 != 0)
		{
			cc_array[counter] *= 2
		}
		
		digit_string += cc_array[counter]
	
	}
	
	digit_sum = 0
	
	for ( counter=0; counter<digit_string.length; counter++ )
	{
		current_digit = parseInt( digit_string.charAt(counter) )
		digit_sum += current_digit
	}
	
	if ( digit_sum %% 10 == 0 )
	{
		return true
	}
	else
	{
		return false
	}

}


                        
	  
            function ifLoggedIn(){

            var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );


                        
                        if(results){

                        document.getElementById('4').innerHTML="LOG-OUT"
                        
                        }

        


            }

	    function loadXMLDoc(obj)

	    
		{
		if (window.XMLHttpRequest)
		  {
		  xmlhttp=new XMLHttpRequest();
		  }
		else
		  {
		  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		  }
		xmlhttp.onreadystatechange=function()
		  {
		  if(xmlhttp.readyState==4)
			{
                                
                        document.getElementById("mySearch").innerHTML=xmlhttp.responseText;

                        
			}
		  }

                if(obj.id==1){
		
		xmlhttp.open("GET","newReleases1.py",true);
		xmlhttp.send();}

                else if(obj.id==2){

                xmlhttp.open("GET","newAdditions1.py",true);
		xmlhttp.send(); }


		else if(obj.id==3){

                    xmlhttp.open("GET","assign3_q61.py",true);
		    xmlhttp.send();}



            else if(obj.id==5){
                

                    
                    var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

                    if(results){
                        xmlhttp.open("GET","updatecust.py?cust_id="+%s,true);
		        xmlhttp.send();}

		    else{
                        alert('You have to login');
		    }

                }    
            






                else if(obj.id==6){
                
                    
                    var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

                    if(results){
                        xmlhttp.open("GET","cust_history.py?cust_id="+%s,true);
		        xmlhttp.send();}

		    else{
                        alert('You have to login');
		    }

                }    
            


		else if(obj.id=="genre"){

                        xmlhttp.open("GET","searchByGenre.py?choice="+obj.value,true);
                        xmlhttp.send();}


                else if(obj.id=="signin_submit"){


                cc=document.getElementById('field').value
                pass=document.getElementById('password').value
                firstname=document.getElementById('firstname').value
                lastname=document.getElementById('lastname').value
                phonenum=document.getElementById('phonenum').value
                billadd=document.getElementById('billadd').value
                shipadd=document.getElementById('shipadd').value
                          
                if(luhn_check(cc)==false)
                    alert('Enter a proper card number')

                 else{

                      
                    xmlhttp.open("GET","insertupdatecustomer.py?cust_id="+%s+"&ccn="+cc+"&password="+pass+"&firstname="+firstname+"&lastname="+lastname+"&bill_addr="+billadd+"&ship_addr="+shipadd+"&phonenum="+phonenum,true)
                    //+"&ccn="+cc+"&password="+password+"&firstname="+firstname+"&lastname="+lastname+"&bill_addr="+billadd+"&ship_addr="+shipadd+"&phonenum="+phonenum,true);

                   
                    xmlhttp.send();
                    alert('entered')


                 }
                    
                    



                }



                else if(obj.id=="submit"){

                        

                        val1=document.getElementById("Search").value;

                        
                        val2=document.getElementById("category").value;

                        

                        xmlhttp.open("GET","assign3_start1.py?submit="+val1+"&category="+val2,true);
                        xmlhttp.send();


                }

                else if(obj.id==4 && obj.innerHTML=="LOG-IN"){

                    window.location.replace("final_login.py");

                }

                else if(obj.id==4 && obj.innerHTML=="LOG-OUT"){

                    window.location.replace("navbar_ver1.py");
                    destroyCookie();

                }


            

                else if(obj.id=="xaction"){        

                        
        	
                        var pass="reserved=";

                        var x1=document.getElementById('table').rows.length;
                        
                        for(i=1;i<x1;i++){
                        var x=document.getElementById('table').rows[i].cells;
                        z=document.getElementById(""+(i-1));
                        if(z.checked){
                        pass+=x[0].innerHTML+"_";}
                        }

                        var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );


                        
                        if(results){
                        xmlhttp.open("GET","renting.py?"+pass,true);
                        xmlhttp.send();
                        }
                        else{
                        alert('you have to log-in');
                        

                        }
                        }

           
                    }


                      function destroyCookie(){

                            var cookie_date =new Date();  // current date & time
                            cookie_date.setTime(cookie_date.getTime()-1);
                            document.cookie = "cooks" + "=; expires=" + cookie_date.toGMTString();

                          }

		</script>

		

		<link rel="stylesheet" href="/htdocs/others/mystyle.css">
		</head> 
		<body onload="ifLoggedIn()">

		<form>
              
		<div id="navbar"> 
		  <ul> 
                                
				<li><button id="1" type="button" onclick="loadXMLDoc(this)">NEW RELEASES</button></li> 
				<li><button id="2" type="button" onclick="loadXMLDoc(this)">NEW ADDITIONS</button></li> 
				<li><button id="3" type="button" onclick="loadXMLDoc(this)">MOST POPULAR</button></li>
                                <li><button id="4" type="button" onclick="loadXMLDoc(this)">LOG-IN</button></li>
                                <li><button id="5" type="button" onclick="loadXMLDoc(this)">ACCOUNT UPDATE</button></li>
				<li><button id="6" type="button" onclick="loadXMLDoc(this)">MY TRANSACTIONS</button></li> 
                                <li> <form>            
                                <select name="choice" id="genre" onclick="loadXMLDoc(this)">
                                <option value="action">Action</option>
                                <option value="adventure">Adventure</option>
                                <option value="drama">Drama</option>
                                <option value="documentary">Documentary</option>
                                </select> </form> </li> 
				
            
            
				
		  </ul> 
		</div> 
                </form>

		<table>
		

		<p align="center">Janet's Video Store</p>

		<!--insert the picture-->
		<tr>
		<h2 align="center">
			<input style="WIDTH: 221px; HEIGHT: 181px" src="/htdocs/others/movie_clipboard.gif" size=12 
			  type=image name=clip> </h2>

		</tr>

		<!--search bar-->

		<tr>

				<form><br/>      		
					<p align="center"><input type="text" style="WIDTH: 200px; HEIGHT: 15px" size=28 id="Search">&nbsp;
			  
			  
					<select id="category" style="WIDTH: 89px" size=1>
					<option selected value="movie">Movie</option>
					<option value="actor">Actor</option> 
					<option value="director">Director</option></select> 

			  <input id="submit" value="Search" type="button" onclick="loadXMLDoc(this)"> </p>


			</form>
		</tr>
                    
		<tr>
		
		<hr>
		<div id="mySearch"><b>RESULTS WILL BE DISPLAYED HERE</b></div>
		</hr>
		</tr>
		</table>

                
                
		</body> 
		</html>

		'''%(cust_id,cust_id,cust_id)
    except:
            http_headers()
            print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
            cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
    print "Content-Type: text/html\n"
    
run()
