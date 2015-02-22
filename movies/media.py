class Movie():
    """This class builds movie information to be displayed in a web browser"""

    # Initalizes an instance of Movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb_rating, cast):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_rating = imdb_rating
        self.cast = cast

    # Sets the storyline of a Movie instance
    def set_storyline(self, storyline):
        self.storyline = storyline

    # Sets the poster url of a Movie instance
    def set_poster(self, poster):
        self.poster_image_url = poster

    # Sets the IMDB rating of a Movie instance
    def set_imdb(self, imdb):
        self.imdb_rating = imdb

    # Sets the cast of a Movie instance
    def set_cast(self, actors):
        self.cast = actors
