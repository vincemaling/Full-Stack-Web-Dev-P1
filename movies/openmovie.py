import requests
import json
import fresh_tomatoes
import media

# This URL is for the Open Movies Database API, which I will use to append IMDB ratings, poster URLs, and other data to my movies
OM_URL = "http://www.omdbapi.com/?"

# This declaration creates a list of my favorite Bogie movies; the blanks will be filled in later
movie_list = [media.Movie('The Big Sleep', '', '', 'http://youtu.be/VjJlBnfyiI4', '', ''),
              media.Movie('Casablanca', '', '', 'http://youtu.be/EJvlGh_FgcI', '', ''),
              media.Movie('Dark Passage', '', '', 'http://youtu.be/UFd0xohHqTI', '', ''),
              media.Movie('The Maltese Falcon', '', '', 'http://youtu.be/3a9YU1SVbSE', '', ''),
              media.Movie('The African Queen', '', '', 'http://youtu.be/ZUxJ2bes00E', '', '')]

# Loop through the movies, call the Open Movies API, and set Plot, IMDB Ratings, Poster images, and Actors data for each
for movie in movie_list:
    movie_query = movie.title
    payload = {'t': movie_query, 'plot': 'short', 'r': 'json'}
    r = requests.get(OM_URL, params=payload)
    movie_data = json.loads(r.text)
    print movie_data['Title'] + ' | IMDB Rating: | ' + movie_data['imdbRating'] + ' | Poster: | ' + movie_data['Poster']
    movie.set_storyline(movie_data['Plot'])
    movie.set_poster(movie_data['Poster'])
    movie.set_imdb(movie_data['imdbRating'])
    movie.set_cast(movie_data['Actors'])
    
# Finally, call Fresh Tomatoes to render the HTML file
fresh_tomatoes.open_movies_page(movie_list)
