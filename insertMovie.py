#!/usr/bin/env python
import cgi, tmdb
def insertMovie():
    try:
        html = ['''
                <html>
                <body>
                <form name = "input" action = "insertMovie.py" method = "post">
                Insert a movie into the Movie Database. <br />
                Note: TMDb's API will handle populating the movie's fields. <br /><br />
                Movie Title: <input type = "text" name = "movie"/> 
                <input type = "submit" value = "Submit" />
                </input>
                </form>
                ''']
        
        http_headers()
        print "\n".join(html)           
        
        form = cgi.FieldStorage()
        
        if form.has_key("movieID"):
            movie_ID = form["movieID"].value
            movie = tmdb.getMovieInfo(movie_ID)
            
            print "The movie '%s' has been successfully inserted" %movie['name']
        #This is in a try block because the API doesn't always have all the fields filled in.
        #There are some nested try blocks--this is because certain fields (like the poster image or
        #summary) are more unlikely to be unavailable.
            try:
                try:
                    url = movie['images'].posters[0]['cover']
                    html = ['<br /><br /><center><img src="']
                    print "\n".join(html)
                    print url
                    html= ['''" alt="poster" align = "top"/></center><br />''']
                    print "".join(html)
                #image copyright of Town Of Warner(tm)
                except:
                    html = ['''
                            <br /><br /><center><img src="http://www.townofwarner.com/images/businesses
                            /notavailable.gif" alt="poster" align = "top"/></center><br />
                            ''']
                    print "".join(html)
                
                print "<strong>Movie Name:</strong> %s <br /><br />" %movie['name']
                print "<strong>Date Released:</strong> %s <br /><br />" %movie['released']
                
                #Sometimes the API won't successfully show the overview (usually due to
                #an ascii codec error).
                try:
                    print "<strong>Movie Summary:</strong> %s <br /><br />" %movie['overview']
                except:
                    print ""
                
                print "<strong>Movie Director(s):</strong>"
                directors = movie['cast']['director']
                for director in directors:                    
                    print " %s, " %director['name']
    
                print "<br /> <br /><strong>Movie Cast:</strong>"
                cast = movie['cast']['actor']
                for member in cast:                    
                    print " %s, " %member['name']
    
                print "<br /> <br /><strong>Movie Genre(s):</strong>"
                genres = movie['categories']['genre']
                for genre in genres:                    
                    print " %s, " %genre
            except:
                print ""
        
        elif form.has_key("movie"):
            results = tmdb.search(form["movie"].value)
            
            try:
                results[0] #this checks if the list isn't empty
                
                html = ['''
                <br \><p>Based on the list provided below, submit the proper ID number in order to insert the movie.</p>       
                <form name = "movie_input" action = "insertMovie.py" method = "post">
                Movie ID: <input type = "text" name = "movieID" /> 
                <input type = "submit" value = "Submit" /><br \> <br \>
                     ''']
                print "\n".join(html)
                
                #This prints out all of the possible movies based on the movie title the employee writes.
                #It prints the movie's ID, title, and year released (if provided in API).
                for searchResult in results:
                    print tmdb.getMovieInfo(searchResult['id'])['id'] + ": "
                    print tmdb.getMovieInfo(searchResult['id'])['name']
                    
                    year_released = tmdb.getMovieInfo(searchResult['id'])['released']
                    if year_released != None:
                        year_released = year_released.split('-', 1 ) #show only the year, not whole date
                        print "(%s)" %year_released[0]
                        
                    html = ["<br />"]
                    print "\n".join(html)
            except:
                print "The movie could not be found in the API."
                
                #If not found in API, maybe employee can manually insert the movie?     
                
                #Sometimes this will show at the end of the list even though
                #movies have been found. Try typing Transformers; the last
                #item in the list will show this.
    
    except:
        http_headers()
        print "<!-- --> <hr><h1>Oops... an error occurred.</h1>"
        cgi.print_exception()

def http_headers():
    print "Content-Type: text/html\n"
    
insertMovie()