import cgi
import cgitb;cgitb.enable()

def run():
    try:
        html = []
        http_headers()
        print """

        <frameset rows="20%,80%" frameborder="NO" border ="0" id="Frame1">
          <frame src="search_frames.py" name ="Frame_search"/>
          <frameset cols="20%,80%" id="Frame2">
            <frame src="leftframe.py" id="Frame_links" name = "Frame_links"/>
            <frame src="mainframe.py" id="Frame_body" name = "Frame_body"/>
          </frameset>
        </frameset>
    
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
