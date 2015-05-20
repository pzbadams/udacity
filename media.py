import webbrowser

#Creation of the class movie
class Movies():
    """ This class provides a way to store movie related information"""

    
    #Creation of the constructor Movie, that contains instance variables
    def __init__ (self, movie_title, movie_year, movie_rating, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.rating = movie_rating
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Intance method to show the Movie trailer on your Web-browser      
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
