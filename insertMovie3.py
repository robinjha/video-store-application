import MySQLdb
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import urllib




#!/usr/bin/env python

#Employee Interface: Problem 8
'''This uses TMDb API to fill in certain fields in order to insert a movie into
the database. The employee first has to fill out a movie title, and then
through the API, a list of possible movies with related titles will be
displayed. Based on the list, the employee will insert the unique movie ID
number (and also provide a trailer link if available. The API doesn't supply
trailer links, thus the employee has to manually insert one).
Then the movie will be inserted into the database, and the employee will see
a page with the movie's information. There's a lot of try and catch blocks
because the API doesn't always have all the fields.'''

import cgi, tmdb, movieObject

def unicodeConvert(s):
    return unicodedata.normalize('NFKD',s).encode('ascii', 'ignore')

def displayMovieInfo(movie):
#Note: All of the .encode('ascii', 'replace') is to prevent ascii errors. These
#tend to happen,especially with foreign films involved
    
    html = ['''
            <strong>The movie '%s' has been successfully inserted</strong>
            <br /><br /><center><img src="%s" alt="poster" align = "top"/></center><br />
           <strong>Movie Name:</strong> %s <br /><br />
            <strong>Movie Summary:</strong> %s <br /><br />
            <strong>Year Released:</strong> %s <br /><br />
            <strong>Movie Genre:</strong> %s <br /> <br />
            <strong>Trailer URL:</strong> %s <br /><br />
            <strong>Movie Director(s): </strong>
            '''
            %(movie.getTitle().encode('ascii', 'replace'), movie.getPhoto(),
              movie.getTitle().encode('ascii', 'replace'), movie.getSummary().encode('ascii', 'replace'),
              movie.getYear(), movie.getGenre().encode('ascii', 'replace'), movie.getTrailer())] 
    print "\n".join(html)
    
    #since directors and cast names are in a list, couldn't just put everything in
    #one hmtl block. Had to use loops to display results.

    i = 0
    while (i != len(movie.getDirectorsFirst())):
        print "%s %s," %(movie.getDirectorsFirst()[i].encode('ascii', 'replace'), movie.getDirectorsLast()[i].encode('ascii', 'replace'))
        i += 1
        
    print "<br /><br /><strong>Cast: </strong>"
    
    i = 0
    while (i != len(movie.getCastFirst())):
        #A person with a middle name (like Neil Patrick Harris) will have his/her
        #middle name stored in the cast's last name list
        print "%s %s," %(movie.getCastFirst()[i].encode('ascii', 'replace'), movie.getCastLast()[i].encode('ascii', 'replace') )
        i += 1


    db = MySQLdb.connect("localhost","root","pass1","assign3")
    c = db.cursor()
    query="""insert into cast (first_name,last_name) values ('%s','%s')"""%(movie.getCastFirst()[0].encode('ascii', 'replace'),movie.getCastLast()[0].encode('ascii', 'replace'))
    c.execute(query)
    db.commit()
    query="""insert into director (first_name,last_name) values ('%s','%s')"""%(movie.getDirectorsFirst()[0].encode('ascii', 'replace'),movie.getDirectorsLast()[0].encode('ascii', 'replace'))
    c.execute(query)
    db.commit()
    query="""insert into genre (type) values ('%s')"""%(movie.getGenre().encode('ascii', 'replace'))
    c.execute(query)
    db.commit()

    query="""select count(*) from movie"""
    c.execute(query)
    data=c.fetchall()
    movie_id=data[0][0]
    

    query="""select count(*) from cast"""
    c.execute(query)
    data=c.fetchall()
    cast_id=data[0][0]


    query="""select count(*) from director"""
    c.execute(query)
    data=c.fetchall()
    director_id=data[0][0]
    
    query="""select count(*) from genre"""
    c.execute(query)
    data=c.fetchall()
    genre_id=data[0][0]
    




    query="""insert into castmovie (cast_id,director_id,movie_id) values (%s,%s,%s)"""%(cast_id,director_id,movie_id)
    c.execute(query)
    db.commit()

    query="""insert into movie (title,genre_id,pricegroup_id,is_rented,year_release,description,photo,arrival_date,trailer_link) values ('%s',%s,%s,%s,curdate(),'%s',%s,curdate(),%s)"""%(movie.getTitle().encode('ascii', 'replace'),genre_id,1,0,movie.getSummary().encode('ascii', 'replace'),'null','null')
    c.execute(query)
    db.commit()

    db.close()     



    


def insertMovie():
    try:
        html = ['''
                <html>
                <body>
                <form>
                Insert a movie into the Movie Database. <br />
                Note: TMDb's API will handle populating the movie's fields. <br /><br />
                Movie Title: <input type = "text" name = "movie" id="movietitle"/> 
                <input id="searchmovieTitle" type = "button" value = "Submit" onclick="loadXMLDoc(this)" />
                </form>
                ''']
        http_headers()
        print "\n".join(html)           
        
        form = cgi.FieldStorage()
        
        if form.has_key("movieID"):
            movieAPI = tmdb.getMovieInfo(form["movieID"].value)
            movie = movieObject.Movie(movieAPI['name'])
            
            try:
                year_released = movieAPI['released']
                year_released2 = year_released.split('-', 1 ) #show only the year, not whole date
                year_released = year_released2[0]
                movie.setYear(year_released)
            except:
                movie.setYear("Unavailable")
                
            try:
                photo_url = movieAPI['images'].posters[0]['cover']
                movie.setPhoto(photo_url)
            except:
                #Image Unavailable" picture is copyright of Town Of Warner(tm)
                movie.setPhoto("http://www.townofwarner.com/images/businesses/notavailable.gif")
            
            if form.has_key("trailerURL"):
                movie.setTrailer(form["trailerURL"].value)
            else:
                movie.setTrailer("Unavailable")
            
            try:
                genres = movieAPI['categories']['genre']
                movie.setGenre(genres.keys()[0])
            except:
                movie.setGenre("Unavailable")
        
            try:
                directors = movieAPI['cast']['director']
                
                directors_first = []
                directors_last = []
                
                for director in directors:
                    directors_name = director['name'].partition(' ')
                    directors_first.append(directors_name[0])
                    directors_last.append(directors_name[2])
                    
                movie.setDirectorsFirst(directors_first)
                movie.setDirectorsLast(directors_last)
                
            except:
                movie.setDirectorsFirst([])
                movie.setDirectorsLast([])

            try:
                actors = movieAPI['cast']['actor']
                
                actors_first = []
                actors_last = []
                
                for actor in actors:
                    actor_name = actor['name'].partition(' ')
                    actors_first.append(actor_name[0])
                    actors_last.append(actor_name[2])
                    
                movie.setCastFirst(actors_first)
                movie.setCastLast(actors_last)
                
            except:
                movie.setCastFirst([])
                movie.setCastLast([])
                
            try:
                summary = movieAPI['overview']
                movie.setSummary(summary)
            except:
                movie.setSummary("Unavailable")
                
            displayMovieInfo(movie)
            
            
        elif form.has_key("movie"):
            results = tmdb.search(form["movie"].value)
            
            try:
                results[0] #this checks if the movie list isn't empty
                
                html = ['''
                <br \><p><strong>Based on the list provided below, submit the
                    proper ID number in order to insert the movie.</strong></p>
                <p><i>Unfortunately, TMDb API does not supply trailer links. <strong>If applicable</strong>,
                    please also supply a URL for the movie's trailer.</i></p> 
                <form name = "movie_input">
                Movie ID: <input type = "text" name = "movieID"  id="mid"/> <br />
                Trailer URL: <input type = "text" name = "trailerURL" id="turl" /> <br />
                <input type = "button" value = "Submit" onclick="loadXMLDoc(this)" id="fulldetail" /><br \> <br \>
                <strong>LIST OF MOVIES</strong> <br />
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
                
                #Sometimes this will show at the end of the list even though
                #movies have been found. Try typing Transformers; the last
                #item in the list will show this. I think it's an ascii error.
    
        html = ['''
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
    
insertMovie()

