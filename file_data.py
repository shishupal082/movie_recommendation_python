def file_movies_data() :
    given_genres = ["unknown","action","adventure","animation","children's","comedy","crime","documentary","drama","fantasy","film-noir","horror","musical","mystery","romance","sci-fi","thriller","war","western"]
    f = open('movie.data')
    movies_dict = {}
    genres_for_movie = {}
    for line in f:
        i = 5
        tokens = line.split('|')
        genres_for_movie[int(tokens[0])]=[]
        while i < 24  :
            if int(tokens[i]) == 1 :
                genres_for_movie[int(tokens[0])].append(given_genres[i-5])
            i = i+1
        movies_dict[int(tokens[0])]={"movie_watched_count": 0,"movie_total_rating": 0,"movie_id":int(tokens[0]),"movie_title":tokens[1],"release_date":tokens[2],"genres":genres_for_movie[int(tokens[0])]}
    
    
    return movies_dict
    
def file_updated_movies_data() :
    updated_movies_dict = file_movies_data()
    f = open('ratings.data')
    for line in f :
        tokens = line.split('\t')
        updated_movies_dict[int(tokens[1])]["movie_watched_count"] = 1+updated_movies_dict[int(tokens[1])]["movie_watched_count"]
        updated_movies_dict[int(tokens[1])]["movie_total_rating"] = updated_movies_dict[int(tokens[1])]["movie_total_rating"] + int(tokens[2])
    return updated_movies_dict
#if __name__ == "__main__":
    #file_updated_movies_data()
