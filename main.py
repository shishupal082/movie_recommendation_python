import hardcoded_data
def main():

    rating_list = hardcoded_data.hardcoded_rating_data()   
    #Most Watched Movie **************************************
    movie_watched_count = [0]
    i = 0
    max_movie_id = 4
    
    while i < max_movie_id :
        movie_watched_count.append(0)
        i = i+1
        
    i = 0
    while i < len(rating_list) :
        movie_watched_count[rating_list[i]["movie_id"]] = 1 + movie_watched_count[rating_list[i]["movie_id"]]
        i = i+1
    
    i=0 
    x = max(movie_watched_count)
    
    while i < max_movie_id+1 :
        if x == movie_watched_count[i] :
            most_watched_movie_id = i
            print("Most Watched Movie ID = " + str(i))
            break
        i = i+1
    #Top Movie By Genre **************************************
if __name__ == "__main__":
    main()
