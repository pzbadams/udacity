import fresh_tomatoes
import media

#instances of class Movies
clue = media.Movies("Clue",
                    "1985",
                    "PG",
                    "Six guests are invited to a strange house and must cooperate with the staff to solve a murder mystery.",
                    "http://upload.wikimedia.org/wikipedia/en/thumb/1/18/Clue_Poster.jpg/220px-Clue_Poster.jpg",
                    "https://www.youtube.com/watch?v=cDDdeHtrxfA")
hotel = media.Movies("Hotel Rwanda",
                     "2004",
                     "PG-13",
                     "The true story of Paul Rusesabagina, a hotel manager who housed over a thousand Tutsi refugees during their struggle against the Hutu militia in Rwanda.",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Hotel_Rwanda_movie.jpg/220px-Hotel_Rwanda_movie.jpg",
                     "https://www.youtube.com/watch?v=4dd8rX5Dy_Q")
pirates = media.Movies("Pirates of the Caribbean: The Curse of the Black Pearl",
                       "2003",
                       "PG-13",
                       "Blacksmith Will Turner teams up with eccentric pirate Captain Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead.",
                       "http://upload.wikimedia.org/wikipedia/en/thumb/0/0e/Pirates_of_the_Caribbean_movie.jpg/220px-Pirates_of_the_Caribbean_movie.jpg",
                       "https://www.youtube.com/watch?v=0Z1XpfbuZOA")
turino = media.Movies("Gran Torino",
                      "2008",
                      "R",
                      "Disgruntled Korean War veteran Walt Kowalski sets out to reform his neighbor, a Hmong teenager who tried to steal Kowalski's prized possession: a 1972 Gran Torino.",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/c/c6/Gran_Torino_poster.jpg/220px-Gran_Torino_poster.jpg",
                      "https://www.youtube.com/watch?v=9ecW-d-CBPc")
future = media.Movies("Back to the Future",
                      "1985",
                      "PG",
                      "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg",
                      "https://www.youtube.com/watch?v=yosuvf7Unmg")
slumdog = media.Movies("Slumdog Millionaire",
                       "2008",
                       "R",
                       "A Mumbai teen, who grew up in the slums, becomes a contestant on the Indian version of 'Who Wants To Be A Millionaire?' He is arrested under suspicion of cheating, and while being interrogated, events from his life history are shown which explain why he knows the answers.",
                       "http://ia.media-imdb.com/images/M/MV5BMTU2NTA5NzI0N15BMl5BanBnXkFtZTcwMjUxMjYxMg@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=kuSTr48P9mc")
reign = media.Movies("Reign Over Me",
                     "2007",
                     "R",
                     "A man who lost his family in the September 11 attack on New York City runs into his old college roommate. Rekindling the friendship is the one thing that appears able to help the man recover from his grief.",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/7/7c/ReignPoster.jpg/220px-ReignPoster.jpg",
                     "https://www.youtube.com/watch?v=oxkPsxIK4xQ")
mind = media.Movies("A Beautiful Mind",
                    "2001",
                    "PG-13",
                    "After a brilliant but asocial mathematician accepts secret work in cryptography, his life takes a turn for the nightmarish",
                    "http://upload.wikimedia.org/wikipedia/en/thumb/b/b8/A_Beautiful_Mind_Poster.jpg/220px-A_Beautiful_Mind_Poster.jpg",
                    "https://www.youtube.com/watch?v=WFJgUm7iOKw")
blood = media.Movies("Blood Diamond",
                     "2006",
                     "R",
                     "A fisherman, a smuggler, and a syndicate of businessmen match wits over the possession of a priceless diamond.",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Blooddiamondposter.jpg/220px-Blooddiamondposter.jpg",
                     "https://www.youtube.com/watch?v=yknIZsvQjG4")

movies = [clue, hotel, pirates, turino, future, slumdog, reign, mind, blood]
fresh_tomatoes.open_movies_page(movies)
