
def run():
    try:
        http_headers()
        print """
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
			<html xmlns="http://www.w3.org/1999/xhtml"> 
			<head> 
			<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
			<script type="text/javascript" src="http://plugins.learningjquery.com/expander/jquery.expander.js"></script>

			<script type="text/javascript">
			$(document).ready(function() {
			  $("div.expandable p").expander();
			  
			  $("div.expandable p").expander({
				slicePoint:       40,  // default is 100
				collapseTimer:    5000, // re-collapses after 5 seconds; default is 0, so no re-collapsing
				userCollapseText: '[^]'  // default is '[collapse expanded text]'
			  });
			  
			});
			</script>
			</head>

			<body>

			<div class="expandable">
				<p>
				
				 text goes herecfhjvhjgqhjdfvqnhjfbvakjfjBJBVFWBFBwbfjudddddddddddddddddddddddddddddddddddddddddddddddddddddddddc
				 text goes herecfhjvhjgqhjdfvqnhjfbvakjfjBJBVFWBFBwbfjudddddddddddddddddddddddddddddddddddddddddddddddddddddddddc
				</p>
				
			  </div>
			</body>
			</html>
			"""
			
    except:
            http_headers()
            print "<!-- --><hr><h1>Oops...an error occurred.</h1>"

    #Function: http_headers
    #Purpose: Print out the headers so we can show something on the screen.
def http_headers():
	print "Content-Type: text/html\n"

	print
   
run()
