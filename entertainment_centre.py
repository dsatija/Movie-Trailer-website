import fresh_tomatoes

import media

"""Creating instances of class Movie"""

DDLJ = media.Movie("DDLJ", "Raj and Simran meet on a trip to Europe  \
                   and fall in love.The battle begins to win  \
                   over two traditional families.",
                   "http://mashable.com/wp-content/" +
                   "uploads/2015/10/DDLJ-remake.jpg",
                   "https://www.youtube.com/ \
                    watch?v=RCS5NlDIqME")

DTPH = media.Movie("Dil To Pagal hai",
                   "Promised to another via arranged marriage, \
                    a dancer (Madhuri Dixit) falls in love with her  \
                    director (Shahrukh Khan)", "http://www.gstatic.com/tv/" +
                   "thumb/dvdboxart/66025/p66025_d_v7_aa.jpg",
                   "https://www.youtube.com/watch?v=ji5Zk20VQCY")

lagaan = media.Movie("Lagaan", "This is the story about the resilience  \
                      shown by the Indians when they were under the  \
                      British Rule", "http://cdn.bollywoodtabloid.com/" +
                     "wp-content/uploads/2015/07/Lagaan.jpg",
                     "https://www.youtube.com/ \
                     watch?v=oSIGQ0YkFxs")

HDDCS = media.Movie("Hum Dil De Chuke Sanam", "A touching Love Story",
                    "http://www.gstatic.com/tv/thumb/dvdboxart" +
                    "/25517/p25517_d_v7_aa.jpg",
                    "https://www.youtube.com/watch?v=njs8UBO7qHc")

K2H2 = media.Movie("Kuchh Kuchh Hota Hai", "Before dying, a woman \
                   (Rani Mukherjee) leaves letters asking her daughter  \
                   to play matchmaker for her father(Shahrukh Khan)  \
                   and his college friend (Kajol)",
                   "https://upload.wikimedia.org/wikipedia/en/0/07/" +
                   "Kuch_Kuch_Hota_Hai_poster.jpg",
                   "www.youtube.com/watch?v=83rVJ-rRPns")

sathiya = media.Movie("Sathiya", "Two students (Rani Mukherjee, \
                      Vivek Oberoi) meet at a wedding and fall in love, \
                      but they marry in secret due to their class  \
                      differences", "http://ia.media-imdb.com/images/M/" +
                      "MV5BMTkyMDQ4NjI5N15BMl5BanBn" +
                      "XkFtZTgwNTYzOTI0MzE@._V1_SX214_AL_.jpg",
                      "https://www.youtube.com/watch?v=n3r5xifaxqs")

movies = [DDLJ, DTPH, lagaan, HDDCS, K2H2, sathiya]

"""Calling the function to open static web page"""

fresh_tomatoes.open_movies_page(movies)
