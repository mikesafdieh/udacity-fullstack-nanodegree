import webbrowser # for opening youtube videos on webpage

# define class
class Movie():
    # below is the doc string for the Movie class. It will be the value of the built in __doc__ class variable
    """ This class provides a way to store movie related information. """ 

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor
    def __init__(self, title, storyline, poster_image, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        