import media
import fresh_tomatoes
import urllib
import json

#Define movie title array and initialize arrays for movie details
movie_titles = ["The Dark Knight","Shutter Island","Predestination","Inside Out","Gattaca","Memento"]
storylines = [None] * len(movie_titles)
posters = [None] * len(movie_titles)
release_dates = [None] * len(movie_titles)
imdb_ratings = [None] * len(movie_titles)

#Establishes connection to movie database to retrieve movie information and stores information into arrays
for position, movie_title in enumerate(movie_titles):
    connection = urllib.urlopen("http://www.omdbapi.com/?t=" + movie_title)
    output = connection.read()
    connection.close()
    data = json.loads(output)
    storylines[position] = data["Plot"]
    posters[position] = data["Poster"]
    release_dates[position] = data["Released"]
    imdb_ratings[position] = data["imdbRating"]

#Define Movie object informtion
i=0
the_dark_knight = media.Movie(movie_titles[i],
                        storylines[i],
                        posters[i],
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                        release_dates[i],
                        imdb_ratings[i])

i+=1
shutter_island = media.Movie(movie_titles[i],
                        storylines[i],
                        posters[i],
                        "https://www.youtube.com/watch?v=5iaYLCiq5RM",
                        release_dates[i],
                        imdb_ratings[i])

i+=1
predestination = media.Movie(movie_titles[i],
                        storylines[i],
                        posters[i],
                        "https://www.youtube.com/watch?v=jcQacCfi_pw",
                        release_dates[i],
                        imdb_ratings[i])

i+=1
inside_out = media.Movie(movie_titles[i],
                        storylines[i],
                        posters[i],
                        "https://www.youtube.com/watch?v=seMwpP0yeu4",
                        release_dates[i],
                        imdb_ratings[i])

i+=1
gattaca = media.Movie(movie_titles[i],
                        storylines[i],
                        posters[i],
                        "https://www.youtube.com/watch?v=PC6ZA1dFkVk",
                        release_dates[i],
                        imdb_ratings[i])

i+=1
memento = media.Movie(movie_titles[i],
                        storylines[i],
                        posters[i],
                        "https://www.youtube.com/watch?v=nHozKtsvag0",
                        release_dates[i],
                        imdb_ratings[i])

movies = [the_dark_knight, shutter_island, predestination, inside_out, gattaca, memento]
fresh_tomatoes.open_movies_page(movies)
