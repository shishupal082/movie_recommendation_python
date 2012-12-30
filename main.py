from __future__ import division
import hardcoded_data
import file_data

def main():
    
    movies_dict = file_data.file_updated_movies_data()
    
    #movies_dict = hardcoded_data.hardcoded_movies_data()
    print("_____________________________________________________________")
    #****************** Most Watched Movie **************************************
    most_watched_movie_count = 0
    most_watched_movie_id = 0
    for movie_id in movies_dict :
        if movies_dict[movie_id]['movie_watched_count'] > most_watched_movie_count :
            most_watched_movie_count = movies_dict[movie_id]['movie_watched_count']
            most_watched_movie_id = movie_id
    
    print("Most Watched Movie:\t\t\t" + movies_dict[most_watched_movie_id]['movie_title'])
    
    #****************** Top Movie By Genre **************************************
    
    input_genre = "thriller"
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
    print("Top movie by genre'("+input_genre+")':\t"+movies_dict[max_rating_movie_id_in_this_genre]['movie_title'])
    
    #**************** Most Watched Genre ****************************************
    genre_count_dictionary = {"unknown":0,"action":0,"adventure":0,"animation":0,"children's":0,"comedy":0,"crime":0,"documentary":0,"drama":0,"fantasy":0,"film-noir":0,"horror":0,"musical":0,"mystery":0,"romance":0,"sci-fi":0,"thriller":0,"war":0,"western":0}
   
    for movie_id in movies_dict :
        movie_genre_list = movies_dict[movie_id]["genres"]
        for genre in movie_genre_list :
            genre_count_dictionary[genre] = 1 + genre_count_dictionary[genre]
    
    #print(genre_count_dictionary)
            
    max_genre_count = genre_count_dictionary["unknown"]
    genre = "unknown"
    for key_genre in genre_count_dictionary :
        if genre_count_dictionary[key_genre] > max_genre_count :
            max_genre_count = genre_count_dictionary[key_genre]
            genre = key_genre
    
    print("Most Watched Genre:\t\t"+genre)
    
    #**************** Highest Rated Genre ***************************************
    genre_total_rating_dictionary = {"unknown":0,"action":0,"adventure":0,"animation":0,"children's":0,"comedy":0,"crime":0,"documentary":0,"drama":0,"fantasy":0,"film-noir":0,"horror":0,"musical":0,"mystery":0,"romance":0,"sci-fi":0,"thriller":0,"war":0,"western":0}
    
    for movie_id in movies_dict :
        movie_genre_list = movies_dict[movie_id]["genres"]
        movie_rate = movies_dict[movie_id]["movie_total_rating"]/movies_dict[movie_id]["movie_watched_count"]
        for genre in movie_genre_list :
            genre_total_rating_dictionary[genre] = genre_total_rating_dictionary[genre] + movie_rate
    
    #print(genre_total_rating_dictionary)
    genre_rating_dictionary =  {"unknown":0,"action":0,"adventure":0,"animation":0,"children's":0,"comedy":0,"crime":0,"documentary":0,"drama":0,"fantasy":0,"film-noir":0,"horror":0,"musical":0,"mystery":0,"romance":0,"sci-fi":0,"thriller":0,"war":0,"western":0}
    
    genre_rating_dictionary["unknown"] = genre_total_rating_dictionary["unknown"]/genre_count_dictionary["unknown"]
    for key_genre in genre_rating_dictionary :
        genre_rating_dictionary[key_genre] = genre_total_rating_dictionary[key_genre]/genre_count_dictionary[key_genre]
    
    #print(genre_rating_dictionary)
    max_genre_rating = genre_rating_dictionary["unknown"]
    genre = "unknown"
    for key_genre in genre_rating_dictionary :
        if genre_rating_dictionary[key_genre] > max_genre_rating :
            max_genre_rating = genre_rating_dictionary[key_genre]
            genre = key_genre
    
    print("Highest Rated Genre:\t\t"+genre)
    
    print("_____________________________________________________________")
if __name__ == "__main__":
    main()
