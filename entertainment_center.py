import fresh_tomatoes
import media

#Creating instances from movie Class.
oceans_eleven = media.Movie("Ocean's Eleven",
                            "Danny Ocean and his eleven accomplices plan to rob three Las Vegas casinos simultaneously.",
                            "https://upload.wikimedia.org/wikipedia/pt/a/af/Ocean%27s_Eleven_Poster.jpg",
                            "https://www.youtube.com/watch?v=imm6OR605UI",
                            "117 minutes")

the_butterfly_effect = media.Movie("The Butterfly Effect",
                                   "Evan Treborn suffers blackouts during significant events of his life. As he grows up, he finds a way to remember these lost memories and a supernatural way to alter his life by reading his journal.",
                                   "https://upload.wikimedia.org/wikipedia/en/4/43/Butterflyeffect_poster.jpg",
                                   "https://www.youtube.com/watch?v=D4OHgw8jNDQ",
                                   "119 minutes")

the_judge = media.Movie("The Judge",
                        "Big-city lawyer Hank Palmer returns to his childhood home where his father, the town's judge, is suspected of murder. Hank sets out to discover the truth and, along the way, reconnects with his estranged family.",
                        "https://upload.wikimedia.org/wikipedia/en/6/61/The_Judge_2014_film_poster.jpg",
                        "https://www.youtube.com/watch?v=8ikeVQ8WAcQ",
                        "141 minutes")

limitless = media.Movie("Limitless",
                        "With the help of a mysterious pill that enables the user to access one hundred percent of his brain abilities, a struggling writer becomes a financial wizard, but it also puts him in a new world with lots of dangers.",
                        "https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",
                        "https://www.youtube.com/watch?v=4TLppsfzQH8",
                        "105 minutes")
  
the_prestige = media.Movie("The Prestige",
                           "After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other.",
                           "https://upload.wikimedia.org/wikipedia/pt/8/8c/The_Prestige.jpg",
                           "https://www.youtube.com/watch?v=JucYLWfFiAs",
                           "130 minutes")

catch_me_if_you_can = media.Movie("Catch Me If You Can",
                                  "A seasoned FBI agent pursues Frank Abagnale Jr. who, before his 19th birthday, successfully forged millions of dollars' worth of checks while posing as a Pan Am pilot, a doctor, and a legal prosecutor.",
                                  "https://upload.wikimedia.org/wikipedia/pt/thumb/c/c1/Catch_Me_If_You_Can_Capa.jpg/220px-Catch_Me_If_You_Can_Capa.jpg",
                                  "https://www.youtube.com/watch?v=SosRcIMCr5g",
                                  "141 minutes")

#List with movies
movies = [oceans_eleven, the_butterfly_effect, the_judge, limitless, the_prestige, catch_me_if_you_can]

#Function that build the HTML file
fresh_tomatoes.open_movies_page(movies)