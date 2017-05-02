import media # for using the Movie class
import fresh_tomatoes # for webpage generation

# Toy Story data
toy_story = media.Movie( # instantiate Movie instance
    "Toy Story",  # title
    "A story of a boy, and his toys that come to life.", # storyline
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # image url
    "https://www.youtube.com/watch?v=KYz2wyBy3kc" # trailer url
)

# Pirates of the Caribbean: The Curse of the Black Pearl data
pirates = media.Movie(
    "Pirates of the Caribbean",
    "Will Turner teams up with cunning Captain Jack Sparrow to chase the cursed pirates of the Black Pearl, to save his beloved Elizabeth Swan.",
    "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
    "https://www.youtube.com/watch?v=naQr0uTrH_s"
)

# Happy Gilmore data
happy_gilmore = media.Movie(
    "Happy Gilmore",
    "Short tempered Happy Gilmore plays golf to save his grandmother\'s house.",
    "https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",
    "https://www.youtube.com/watch?v=y1emDAYCfVQ"
) 

# The Prince of Egypt data
prince_of_egypt = media.Movie(
    "The Prince of Egypt",
    "Story of the Biblical Exodus of the Isrealites from their enslavement in Egypt.",
    "https://upload.wikimedia.org/wikipedia/en/6/6c/Prince_of_egypt_ver2.jpg",
    "https://www.youtube.com/watch?v=yWs81poMgiM"
)

# Accepted data
batman = media.Movie(
    "Batman Begins",
    "Billionare Bruce Wayne dons the persona of the Batman to save Gotham City",
    "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
    "https://www.youtube.com/watch?v=neY2xVmOfUM"
)

# Warrior data
warrior = media.Movie(
    "Warrior",
    "Two brothers fight in MMA cage wrestling to settle their own distinct issues.",
    "https://upload.wikimedia.org/wikipedia/en/e/e3/Warrior_Poster.jpg",
    "https://www.youtube.com/watch?v=I5kzcwcQA1Q"
)

# create a list of all the Movie instances
movies_list = [toy_story, pirates, happy_gilmore, prince_of_egypt, batman, warrior]

# send list of Movies to be processed and displayed on webpage
fresh_tomatoes.open_movies_page(movies_list)





