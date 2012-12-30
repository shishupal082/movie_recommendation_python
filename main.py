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
    
    print(movies_dict[most_watched_movie_id]['movie_title'])
    #Top Movie By Genre **************************************
    

if __name__ == "__main__":
    main()
