import fresh_tomatoes
import media

#Movie: A Beautiful Mind: Instance created: title, storyline, movie image and movie trailer.
a_beautiful_mind = media.Movie("A Beautiful Mind", "A human drama inspired by "
                "events in the life of mathematical genius, John Forbes Nash Jr.", 
                "https://images-na.ssl-images-amazon.com/images/I/71AHkwimfJL._SY550_.jpg", 
                "https://www.youtube.com/watch?v=YWwAOutgWBQ")

#Movie: Lucy: Instance created: title, storyline, movie image and movie trailer.
lucy = media.Movie("Lucy", 
    "A woman, accidentally caught in a dark deal, turns the tables on her captors "
    "and transforms into a merciless warrior evolved beyond human logic.",
    "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_%282014_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=MVt32qoyhi0")

#Movie: Wonder Woman: Instance created: title, storyline, movie image and movie trailer.
wonder_woman = media.Movie("Wonder Woman", 
            "Diana, princess of the Amazons, trained to be an unconquerable "
            "warrior. Raised on a sheltered island paradise, when a pilot crashes"
            " on their shores and tells of a massive conflict raging in the outside "
            "world, Diana leaves her home, convinced she can stop the threat. "
            "Fighting alongside man in a war to end all wars, Diana will discover "
            "her full powers and her true destiny.",
            "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
            "https://www.youtube.com/watch?v=VSB4wGIdDwo")

#Movie: Pursuit of Happyness: Instance created: title, storyline, movie image and movie trailer.
pursuit_of_happyness = media.Movie("Pursuit of Happyness",
                    "A struggling salesman takes custody of his son as he's poised "
                    "to begin a life-changing professional career.",
                    "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

#Movie: The Notebook:  Instance created: title, storyline, movie image and movie trailer.
the_notebook = media.Movie("The Notebook", 
            "In 1940s South Carolina, mill worker Noah Calhoun (Ryan Gosling) and rich girl "
            "Allie (Rachel McAdams) are desperately in love. But her parents don't approve. "
            "When Noah goes off to serve in World War II, it seems to mark the end of their "
            "love affair. In the interim, Allie becomes involved with another man. "
            "But when Noah returns to their small town years later, on the cusp of "
            "Allie's marriage, it soon becomes clear that their romance is anything but over.",
            "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
            "https://www.youtube.com/watch?v=S3G3fILPQAU")

#Movie: RV: Instance created which includes three variables:  title, storyline, movie image and movie trailer.
rv = media.Movie("RV",
    "The Munros are a typically American dysfunctional family, complete with "
    "rebellious, uncommunicative offspring and baffled parents. Patriarch Bob "
    "would like to remedy the situation before his son and daughter instant-message "
    "their parents out of their lives. Bob rents a motor home to take the clan on "
    "vacation but soon finds that camping and togetherness can be hazardous to "
    "one's health",
    "https://upload.wikimedia.org/wikipedia/en/0/0f/Rv-movieposter.jpg", 
    "https://www.youtube.com/watch?v=QkZXAB-RdbI")

#Variable movies created  to include an array of all movies to be initialized from import fresh_tomatoes
movies = [a_beautiful_mind, lucy, wonder_woman, pursuit_of_happyness, the_notebook, rv]

#Open movie function which includes argument from array of movies 
fresh_tomatoes.open_movies_page(movies)
