#welcome to entertainment center! 
import media 
import fresh_tomatoes
#toy_story = media.Movie("Toy Story",
#                        "A story of a boy and his friends come to life",
#                        "http://www.google.com",
#                        "https://www.youtube.com")
#print(toy_story.storyline)
#avatar = media.Movie("Avatar",
#                     "A marine on an alien planet",
#                     "http://google.",
#                     "http:")
#print(avatar.storyline)
#toy_story.show_trailer()
her = media.Movie("Her","A lonely writer develops an unlikely relationship with his newly purchased operating system that's designed to meet his every need.","http://ia.media-imdb.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=WzV6mXIOVl4")
#her.show_trailer()
matrix = media.Movie("The Matrix","A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.","http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg","https://www.youtube.com/watch?v=m8e-FF8MsqU")

transcendence = media.Movie("Transcendence","Transcendence","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRN0HPCijFUJBdF88DOO_G311EVxGJUBdSZBRM5yGBgQCzyKYa_Jg","https://www.youtube.com/watch?v=VCTen3-B8GU")

interstellar = media.Movie("Interstellar","A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.","http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=2LqzF5WauAw")

avenger = media.Movie("Avengers: Age of Ultron","When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it's up to Earth's Mightiest Heroes to stop the villainous Ultron from enacting his terrible plans.","https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg","https://www.youtube.com/watch?v=tmeOjFno6Do")

terminator = media.Movie("Terminator Genisys","John Connor sends Kyle Reese back in time to protect Sarah Connor, but when he arrives in 1984, nothing is as he expected it to be.","http://ia.media-imdb.com/images/M/MV5BMjM1NTc0NzE4OF5BMl5BanBnXkFtZTgwNDkyNjQ1NTE@._V1_SX214_AL_.jpg","https://www.youtube.com/watch?v=jNU_jrPxs-0")
movies = [her,matrix,transcendence,interstellar,avenger,terminator]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__module__)
