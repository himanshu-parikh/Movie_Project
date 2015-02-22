__author__ = 'himanshuparikh'
# Import our media class, used to create instances of movie objects
import media

# Import fresh_tomatoes  file to display our movies in web format.
import fresh_tomatoes

# First Movie The Dark Knight Movie Details
the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                              "http://a1.mzstatic.com/us/r1000/003/Music/db/24/b1/mzi.wevryeas.200x200-75.jpg",
                              "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

# Second Movie Taken Movie Details
taken = media.Movie("Taken",
                    "A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter, who has been kidnapped while on a trip to Paris.",
                    "http://www.heyuguys.com/images/2010/12/Taken-Quad.jpg",
                    "https://www.youtube.com/watch?v=V35Y8xvbHsE")

# Third Movie Iron Man Details
iron_man = media.Movie("Iron Man",
                       "After being held captive in an Afghan cave, an industrialist creates a unique weaponized suit of armor to fight against evil.",
                       "http://ecx.images-amazon.com/images/I/515wjJQt2nL.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

# Fourth Movie Mission Impossible Details
mission_impossible = media.Movie("Mission Impossible","An American agent, under false suspicion of disloyalty, must discover and expose the real spy without the help of his organization.",
                                 "http://upload.wikimedia.org/wikipedia/en/e/e1/MissionImpossiblePoster.jpg",
                                 "https://www.youtube.com/watch?v=C4g7G_X7Eyc")

#Movies array to be passed into open_movies_page function in fresh_tomatoes file
movies = {the_dark_knight,taken, iron_man, mission_impossible}

# Display movies in a webpage
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)


#Debugging scripts to make sure everything is working good.
#print(the_dark_knight.storyline)
#print(taken.storyline)
#print(iron_man.storyline)
#taken.show_trailer()