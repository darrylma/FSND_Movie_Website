import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G","PG","PG-13","R"]

    #Defines what information to be stored for each movie object
    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, movie_trailer_youtube_url, movie_release_date, movie_imdb_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
        self.release_date = movie_release_date
        self.imdb_rating = movie_imdb_rating

#    def show_trailer(self):
#        webbrowser.open(self.trailer_youtube_url)
