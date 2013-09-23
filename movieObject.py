#Would be more flexible with databases, but it didn't seem hw wanted us to implement one
class Movie:
    cast_first_names = None
    cast_last_names =  None
    directors_first_names = None
    directors_last_names =  None

    pricegroup_name = None
    price = None
    
    genre = None
    
    title = None
    is_rented = None #need this?
    year_released = None
    summary = None 
    
    photo_url = None
    
    arrival_date = None #need this?
    trailer_url = None
    
    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getYear(self):
        return self.year_released
    def setYear(self, year_released):
        self.year_released = year_released

    def getPhoto(self):
        return self.photo_url
    def setPhoto(self, photo_url):
        self.photo_url = photo_url
        
    def getTrailer(self):
        return self.trailer_url
    def setTrailer(self, trailer_url):
        self.trailer_url = trailer_url

    def getGenre(self):
        return self.genre
    def setGenre(self, genre):
        self.genre = genre

    def getDirectorsFirst(self):
        return self.directors_first_names
    def setDirectorsFirst(self, directors_first_names):
        self.directors_first_names = directors_first_names
    
    def getDirectorsLast(self):
        return self.directors_last_names
    def setDirectorsLast(self, directors_last_names):
        self.directors_last_names = directors_last_names

    def getCastFirst(self):
        return self.cast_first_names
    def setCastFirst(self, cast_first_names):
        self.cast_first_names = cast_first_names
    
    def getCastLast(self):
        return self.cast_last_names
    def setCastLast(self, cast_last_names):
        self.cast_last_names = cast_last_names
        
    def getSummary(self):
        return self.summary
    def setSummary(self, summary):
        self.summary = summary