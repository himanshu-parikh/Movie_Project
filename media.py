__author__ = 'himanshuparikh'
# Import the webbrowser library to use in our project
import webbrowser
# Definition of our Movie Class
class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = {"G","PG","PG-13","R"}

    # Initialize our object with the init constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #populate Instance Variables with the passed in object.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # show_trailer Instance Method for displaying the trailer for a particular movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)