#!/usr/bin/env python
import cgi


def test2():
    try:
        http_headers()
        
        s = "This will be a very long string.This will be a very long string.This will be a very long string.This will be a very long string.This will be a very long string.This will be a very long string.This will be a very long string."
        form = cgi.FieldStorage()
        
        html = ['''
                <html>
                <body>
                
                <table border="1">
                <tr>
                <td>
                ''']
        
        if form.has_key("readmore"):
            x = 0
            y = 41
            while x < len(s):
                html += [s[x:y], "<br \>"]
                x+=41
                y += 41
            
            html += [ '''
                <form method = "post" action = "">
                <input type="submit" name = "readless" value="Read Less"  />
                </form></td>''']
        else:
            if len(s) > 15:
                html += [s[0:15], "..."]
            else:
                html += [s]
            
            html += ['''
                     <form method = "post" action = "">
                     <input type="submit" name = "readmore" value="Read More"  />
                     </form></td>''']

        html += ['''
                 
                <td>Row 1, cell 2</td>
                </tr>
                </table>
                </body>
                </html>
                ''']
        print "\n".join(html)    
    except:
        http_headers()
        print "<!-- --> <hr><h1>Oops... an error occurred.</h1>"
        cgi.print_exception()

def http_headers():
    print "Content-Type: text/html\n"
    
test2()




