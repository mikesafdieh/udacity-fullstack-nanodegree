import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of a boy, and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)
# toy_story.show_trailer()

# movies = [toy_story]
# fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS) # VALID_RATINGS is a class variable for the Movie class in the media module
print(media.Movie.__doc__) # __doc__ is a predefined class variable in Python
print(media.Movie.__name__)
print(media.Movie.__module__)