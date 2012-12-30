def hardcoded_rating_data() :
    rating_dict = []
    rating_dict_obj1 = {"user_id":2,"movie_id":1,"rate":4}
    rating_dict_obj2 = {"user_id":1,"movie_id":1,"rate":2}
    rating_dict_obj3 = {"user_id":4,"movie_id":4,"rate":3}
    rating_dict_obj4 = {"user_id":3,"movie_id":3,"rate":5}
    rating_dict.append(rating_dict_obj1)
    rating_dict.append(rating_dict_obj2)
    rating_dict.append(rating_dict_obj3)
    rating_dict.append(rating_dict_obj4)
    return rating_dict
    
def hardcoded_genre_data() :
    genre_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    return genre_list
    
def hardcoded_movies_data() :
    movies_dict = {}
    
    movie_genre1 = ["animation","children's","comedy"]
    movies_dict[1] ={"movie_watched_count":6,"movie_total_rating":19,"movie_id":1,"movie_title":"Toy Story (1995)","release_data":"01-Jan-1995","genres": movie_genre1}
    movie_genre2 = ["comedy","crime","drama"]
    movies_dict[2] ={"movie_watched_count":2,"movie_total_rating":8,"movie_id":2,"movie_title":"GoldenEye (1995)","release_data":"01-Jan-1995","genres": movie_genre2}
    
    return movies_dict
