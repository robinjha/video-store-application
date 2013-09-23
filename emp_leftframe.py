#!/usr/bin/env python

#!/usr/bin/python



def run():
    try:
        http_headers()
        
        print """
        <html>

        <head>
        <h1 align="center">Janet's Video Store (Employee Interface)</h1>
          <title> the Movie DB </title>
          <link rel="stylesheet" href="/htdocs/others/mystyle.css">
          <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
	  <script type="text/javascript" src="http://plugins.learningjquery.com/expander/jquery.expander.js"></script>
	    <script src="http://code.jquery.com/jquery-latest.js"></script>
			
			<script type="text/javascript"> 
			function flipper(){
			$(".flip").click(function(){
				$(".panel").slideToggle("slow");
			  });
			}
			</script>
			 
			<style type="text/css"> 
			div.panel,p.flip
			{
			margin:0px;
			padding:5px;
			text-align:center;
			background:#e5eecc;
			border:solid 1px #c3c3c3;
			}
			div.panel
			{
			height:260px;
			display:none;
			}
			
			</style>















	  <script type="text/javascript">        
			

       function checkStatus(){


       var results = document.cookie.match( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

       if(results){
           
           document.getElementById('8').innerHTML='LOG_OUT';
           
        }
       else{
         document.getElementById('8').style.display='none';
         window.location="navbar_ver1.py"}  

       }


       










        function destroyCookie(){

                            var cookie_date =new Date();  // current date & time
                            cookie_date.setTime(cookie_date.getTime()-1);
                           document.cookie = "cooks" + "=; expires=" + cookie_date.toGMTString();
                           window.location="navbar_ver1.py"

                          }

        function testing(obj){
                      
                      $("div.expandable p").expander({
                            slicePoint:       40,  // default is 100
                            collapseTimer:    15000, // re-collapses after 5 seconds; default is 0, so no re-collapsing
                            userCollapseText: '[^]'  // default is '[collapse expanded text]'
                      });
                      obj.onclick=null;
                
        }
      













    function loadXMLDoc(obj){

          
                
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

                    window.open('navbar_ver1.py')

                }



                else if(obj.id==2){

                

                xmlhttp.open("GET","newAdditions.py",true);
                
		xmlhttp.send();

                
                
		}


		else if(obj.id==3){

                    xmlhttp.open("GET","assign3_q6.py",true);
		    xmlhttp.send();}

               else if(obj.id==4){

              

                xmlhttp.open("GET","createNewEmp.py",true);
		xmlhttp.send();

               } 



               else if(obj.id==5){

                xmlhttp.open("GET","insertMovie3.py",true);
		xmlhttp.send();


               } 



               else if(obj.id==6){

                    xmlhttp.open("GET","emp_5.py",true);
		    xmlhttp.send();}
 

                else if(obj.id==7){

                    xmlhttp.open("GET","emp_6.py",true);
		    xmlhttp.send();}


                else if(obj.id=="empaccount"){
                    xmlhttp.open("GET","insertEmp.py?username="+document.getElementById('username').value+"&password="+document.getElementById('password').value+"&firstname="+document.getElementById('firstname').value+"&lastname="+document.getElementById('lastname').value+"&phonenum="+document.getElementById('phonenum').value+"&address="+document.getElementById('address').value+"&zipcodeid="+document.getElementById('zipcodeid').value,true);
		    xmlhttp.send();


                }    

		 

		else if(obj.id=="genre"){

                        xmlhttp.open("GET","searchByGenre.py?choice="+obj.value,true);
                        xmlhttp.send();}

                else if(obj.id=="general"){

                        

                        val1=document.getElementById("Search").value;

                        
                        val2=document.getElementById("category").value;

                        

                        xmlhttp.open("GET","assign3_start.py?submit="+val1+"&category="+val2,true);
                        xmlhttp.send();


                }
            

                else if(obj.id=="drop_down" && document.getElementById("option_box").value=="rentout"){        

                        var cust_id="";
        	
                        var pass="reserved=";

                        var x1=document.getElementById('table').rows.length;
                        
                        for(i=1;i<x1;i++){
                        var x=document.getElementById('table').rows[i].cells;
                        z=document.getElementById(""+(i-1));
                        if(z.checked){
                        pass+=x[0].innerHTML+"_";}
                        }

                        var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

                        pass+="&cust_id="+document.getElementById("custid").value;
                        
                        if(results){
                        xmlhttp.open("GET","renting_employee.py?"+pass,true);
                        xmlhttp.send();
                        }
                        else{
                        alert('you have to log-in');
                        

                        }
                        }

                else if(obj.id=="drop_down" && document.getElementById("option_box").value=="customer_history"){

                        

                        var pass="?cust_id="+document.getElementById("custid").value;
                        
                        
                        xmlhttp.open("GET","cust_history.py"+pass,true);
                        xmlhttp.send();
                        
                       
                        }

                else if(obj.id=="searchmovieTitle"){


                        var pass="?movie="+document.getElementById('movietitle').value


                       
                       xmlhttp.open("GET","insertMovie3.py"+pass,true);
                        xmlhttp.send();
                        

                }


                else if(obj.id=="fulldetail"){

                    var pass="?movieID="+document.getElementById('mid').value+"&trailerURL="+document.getElementById('turl').value

                     xmlhttp.open("GET","insertMovie3.py"+pass,true);
                        xmlhttp.send();
                          


                }    

                    
                else if(obj.id=="drop_down" && document.getElementById("option_box").value=="return"){

                        

                        var pass="?cust_id="+document.getElementById("custid").value;
                        
                        
                        xmlhttp.open("GET","emp_2.py"+pass,true);
                        xmlhttp.send();
                        
                       
                        }

           
                    
                    
                    else if(obj.id=="xaction_return"){        

                        var cust_id="";
        	
                        var pass="reserved=";

                        var x1=document.getElementById('return_table').rows.length;
                        
                        for(i=1;i<x1;i++){
                        var x=document.getElementById('return_table').rows[i].cells;
                        z=document.getElementById(""+(i-1));
                        if(z.checked){
                        pass+=x[1].innerHTML+"_";}
                        }

                        var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

                        pass+="&cust_id="+document.getElementById("custid").value;
                        
                        if(results){
                        xmlhttp.open("GET","returning.py?"+pass,true);
                        xmlhttp.send();
                        }
                        else{
                        alert('you have to log-in');
                        

                        }
                        }

                    else if(obj.id=="drop_down" && document.getElementById("option_box").value=="update"){


                        var results = document.cookie.match ( '(^|;) ?' + "cooks" + '=([^;]*)(;|$)' );

                        pass="cust_id="+document.getElementById("custid").value;
                        
                        if(results){
                        xmlhttp.open("GET","updatecust.py?"+pass,true);
                        xmlhttp.send();
                        }
                        else{
                        alert('you have to log-in');
                        

                        }}



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

                      
                    xmlhttp.open("GET","insertupdatecustomer.py?cust_id="+document.getElementById("custid").value+"&ccn="+cc+"&password="+pass+"&firstname="+firstname+"&lastname="+lastname+"&bill_addr="+billadd+"&ship_addr="+shipadd+"&phonenum="+phonenum,true)
                    //+"&ccn="+cc+"&password="+password+"&firstname="+firstname+"&lastname="+lastname+"&bill_addr="+billadd+"&ship_addr="+shipadd+"&phonenum="+phonenum,true);

                   
                    xmlhttp.send();
                    alert('entered')


                 }
                    

                
                    
                    



                }









                        }


function luhn_check(card_number)
{
	
	cc_array = card_number.split( "" )
	cc_array.reverse()
	digit_string = ""
	
	for ( counter=0; counter < cc_array.length; counter++ )
	{
		current_digit = parseInt( cc_array[counter] )
		
		if (counter%2 != 0)
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
	
	if ( digit_sum % 10 == 0 )
	{
		return true
	}
	else
	{
		return false
	}

}





                        
            </script>

          
        </head>
    <body onload="checkStatus()">
		<table>
		<tr>
                                
				<form><br/>
				<fieldset>
                                <legend>Search by Customer Account Number</legend>
					<p align="center"><input type="text" id="custid" style="WIDTH: 200px; HEIGHT: 20px" size=28 name=Search >&nbsp;
			  
			  
					<select id="option_box" style="WIDTH: 100px" size="1" name="search">
					<option selected value="customer_history">CUSTOMER HISTORY</option>
					<option value="update">NEW/UPDATE CUSTOMER</option> 
					<option value="rentout">RENT OUT</option>
                                        <option value="return">RETURN MOVIE</option>
                                        

					</select>
				

			   <input id="drop_down" value="Search" type="button" name="submit" onclick="loadXMLDoc(this)"> </p></fieldset>


			</form>
		</tr>

               
                <tr>
                                
				<form><br/>
				 <fieldset>
                                <legend>Search the website</legend>
					<p align="center"><input type="text" style="WIDTH: 200px; HEIGHT: 20px" size=28 id="Search">&nbsp;
			  
			  
					<select style="WIDTH: 89px" size=1 id="category">
					<option selected value="movie">Movie</option>
					<option value="actor">Actor</option> 
					<option value="director">Director</option></select>
				

			  <!--<h2 align="center">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -->
			  <input id="general" value="Search" type="button" name="submit" onclick="loadXMLDoc(this)"> </p>
                         </fieldset>

			</form>
		</tr>
    
               

		
		<tr>
		<td>
			<ul class="navbar">
			  <li><button id="1" type="button" onclick="loadXMLDoc(this)">HOME PAGE</li>
			  <li><button id="2" type="button" onclick="loadXMLDoc(this)" >NEW RELEASES</li>
			  <li><button id="3" type="button" onclick="loadXMLDoc(this)" >MOST POPULAR</li>
			  <li><button id="4" type="button" onclick="loadXMLDoc(this)" >CREATE EMPLOYEE</li>
			  <li><button id="5" type="button" onclick="loadXMLDoc(this)" >INSERT MOVIE</li>
			  <li><button id="6" type="button" onclick="loadXMLDoc(this)" >CURRENTLY RENTED</li>
			  <li><button id="7" type="button" onclick="loadXMLDoc(this)" >OVERDUE MOVIES</li>
			  <li><button id="8" type="button" onclick="destroyCookie()">LOG-IN</li>
		 </td>
		 </tr>
        </ul>

                <tr>
		
		<hr>
		<div id="mySearch" class="test"><b>RESULTS WILL BE DISPLAYED HERE</b></div>
		</hr>
		</tr>

        
		</table>
		


		
		</body>
        </html>
        """
        
    except:
        http_headers()
        print "<!-- --><hr><h1>Oops...an error occurred.</h1>"
        cgi.print_exception()

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
    print "Content-Type: text/html\n"
    
run()
