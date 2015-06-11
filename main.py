import fresh_tomatoes
import media
        
pulpFiction = media.Movie("Pulp Fiction",
                    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                    "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=wZBfmBvvotE")


matrix = media.Movie("The Matrix",
                    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                    "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

trainspotting  = media.Movie("Trainspotting ",
                    "Renton, deeply immersed in the Edinburgh drug scene, tries to clean up and get out, despite the allure of the drugs and influence of friends.",
                    "http://ia.media-imdb.com/images/M/MV5BMTg2MzcxNTY3NV5BMl5BanBnXkFtZTgwOTQ5NDQxMDE@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=R2GKVtWsXKY")

sweetAndLowdown = media.Movie("Sweet and Lowdown",
                    "In the 1930s, fictional jazz guitarist Emmet Ray idolizes Django Reinhardt, faces gangsters and falls in love with a mute.",
                    "http://ia.media-imdb.com/images/M/MV5BMjE2MzA5MDQ4NV5BMl5BanBnXkFtZTgwNjI4ODQxMDE@._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=6stUcaJx5f4")

vickyCristinaBarcelona = media.Movie("Vicky Cristina Barcelona",
                    "Two girlfriends on a summer holiday in Spain become enamored with the same painter, unaware that his ex-wife, with whom he has a tempestuous relationship, is about to re-enter the picture.",
                    "http://ia.media-imdb.com/images/M/MV5BMTU2NDQ4MTg2MV5BMl5BanBnXkFtZTcwNDUzNjU3MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=B-RdUcXAKiw")

amadeus = media.Movie("Amadeus",
                    "The incredible story of Wolfgang Amadeus Mozart, told by his peer and secret rival Antonio Salieri - now confined to an insane asylum.",
                    "http://ia.media-imdb.com/images/M/MV5BMTg5NDkwMTk5N15BMl5BanBnXkFtZTYwODg3MDk2._V1_SX214_AL_.jpg",
                    "https://www.youtube.com/watch?v=yIzhAKtEzY0")

movies = [pulpFiction , matrix, trainspotting, sweetAndLowdown, vickyCristinaBarcelona, amadeus]
fresh_tomatoes.open_movies_page(movies)
