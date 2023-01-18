# import spacy module
import spacy

# load the advanced language model
nlp = spacy.load('en_core_web_md')

# open movies.txt file and read lines as list
movies_read = open("movies.txt", "r")
movies_list = movies_read.readlines()

# define the hulk movie description that we will compare with the list of movies
planet_hulk = '''Will he save the world or destroy it? When Hulk becomes too dangerous
 for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a
 planet where he is sold into slavery and trained as a gladiator'''


# Function to take a movie description as parameter and return title of the most similar movie fo list
def most_similar(film_to_compare, movies):
    # define dictionary to store the similarity scores for each film
    movie_dict = {}
    sentence_nlp = nlp(film_to_compare)
    # iterate through each movie in the list to compare each movie with the hulk movie
    for sentence in movies:
        similarity = nlp(sentence).similarity(sentence_nlp)
        # add tuples to dictionary as key,value (movie,similarity)
        key = sentence
        val = similarity
        movie_dict[key] = val

    # return the key with maximum similarity value
    max_sim = max(movie_dict, key=movie_dict.get)

    # print just the movie name by splitting to remove the movie description
    print("The next movie you should watch is: " + max_sim.split(" :")[0])


# call the function to run the programme
most_similar(planet_hulk, movies_list)
