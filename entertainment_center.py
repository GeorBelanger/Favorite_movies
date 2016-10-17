# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:27:33 2016

@author: jorgebelanger
"""
import fresh_tomatoes
import media


inception=media.Movie("Inception", "A professional thief who steals information by infiltrating the subconscious", 
"http://www.warnerbros.com/sites/default/files/inception_keyart.jpg",
"https://www.youtube.com/watch?v=YoHD9XEInc0")

annie_hall=media.Movie("Annie Hall", "The film stars the director as Alvy Singer, who tries to figure out the reasons for the failure of his relationship", 
"https://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg",
"https://www.youtube.com/watch?v=OqVgCfZX-yE")

il_postino=media.Movie("Il postino", "Chilean poet Pablo Neruda forms a relationship with a simple postman who learns to love poetry", 
"http://movieworld.ws/wp-content/uploads/2013/07/Il-postino-1994.jpg",
"https://www.youtube.com/watch?v=XXCC7SdJW1o")

casablanca=media.Movie("Casablanca", "Set during World War II, it focuses on an American expatriate who must choose between his love for a woman and helping her Czech Resistance leader husband escape the Vichy-controlled city of Casablanca to continue his fight against the Nazis", 
"https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
"https://www.youtube.com/watch?v=BkL9l7qovsE")

water_for_elephants=media.Movie("Water for elephants", "Jacob reveals he had a career in the circus business and was present during one of the most infamous circus disasters of all time", 
"https://upload.wikimedia.org/wikipedia/en/6/60/Water_for_Elephants_Poster.jpg",
"https://www.youtube.com/watch?v=_6b2XhXkPpg")

blue_is_the_warmest_color=media.Movie("Blue is the warmest color", "A French teenager discovers desire and freedom when a blue-haired aspiring painter enters her life.", 
"https://upload.wikimedia.org/wikipedia/en/3/3e/La_Vie_d%27Ad%C3%A8le_film_poster.png",
"https://www.youtube.com/watch?v=mEx5SAiONkQ")

movies=[inception, annie_hall, il_postino, casablanca, water_for_elephants, blue_is_the_warmest_color ]

fresh_tomatoes.open_movies_page(movies)
