from __future__ import division
import hardcoded_data
import file_data

def main():

    rating_dict = hardcoded_data.hardcoded_rating_data()
        
    movies_dict = hardcoded_data.hardcoded_movies_data()
    #Most Watched Movie **************************************
    most_watched_movie_count = 0
    most_watched_movie_id = 0
    for movie_id in movies_dict :
        if movies_dict[movie_id]['movie_watched_count'] > most_watched_movie_count :
            most_watched_movie_count = movies_dict[movie_id]['movie_watched_count']
            most_watched_movie_id = movie_id
    
    print("Most Watched Movie:\t" + movies_dict[most_watched_movie_id]['movie_title'])
    
    #Top Movie By Genre **************************************
    
    input_genre = "comedy"
    movie_id_list = []
    for movie_id in movies_dict :
        genre_list = movies_dict[movie_id]["genres"]
        for genre in genre_list :
            if(genre == input_genre) :
                movie_id_list.append(movie_id)
    
    max_rating = 0
    max_rating_movie_id_in_this_genre = 0
    for movie_id in movie_id_list :
        movie_rating = (movies_dict[movie_id]["movie_total_rating"]) / (movies_dict[movie_id]['movie_watched_count'])
        if movie_rating > max_rating :
            max_rating_movie_id_in_this_genre = movie_id
    print("Top movie of genre'"+input_genre+"':\t"+movies_dict[max_rating_movie_id_in_this_genre]['movie_title'])
if __name__ == "__main__":
    main()
