from fastapi import APIRouter

from typing import List


from model import Movie, MovieDetails, Actor
from movie_data import MovieData

import uuid
import difflib
import random
from supabase_main import Supabase

supabase = Supabase()
router = APIRouter()

def publish_movie(movie : Movie):

    #movie.id = uuid.uuid4()
    actors = movie.star_casts
    details : MovieDetails = movie

    del details.star_casts

    print("dump : ", details.model_dump())

    MovieData.append(movie)

    supabase.insert(table="Movie_table", data=details.model_dump())
    return movie

@router.post("/publish")
def publish(movie : Movie):

    movie = publish_movie(movie)

    return {
        "message" : "Movie Successfully published on Movie's Database.",
        "movie" : movie
    }

@router.post("/publish/list")
def publish_list_of_movies(movies : List[Movie]):

    for movie in movies:
        publish_movie(movie)
    
    return {
        "message" : f"{len(movies)} movies successfully published on Movie's Database"
    }



@router.get("/list/movies")
def list_of_movies():
    return MovieData

@router.get("/movie/details")
def get_movie_details_with_id(id : uuid.UUID):

    for movie in MovieData:
        if id == movie.id:
            return movie
        
    return {
        "message" : "No Movie with id specified."
    }



@router.get("/search/movie/name/{movie_name}")
def search_movie_name(movie_name : str):

    searched_movie = []

    for movie in MovieData:
        close_names = difflib.get_close_matches(movie_name, [movie.name])

        if len(close_names) != 0:
            searched_movie.append(movie)

    return searched_movie

@router.get("/search/movie/year")
def search_movie_by_year(start_year : str, end_year : str):

    searched_movie = []

    for movie in MovieData:

        release_year = movie.year_of_release

        if (start_year <= release_year) and (end_year >= release_year):
            searched_movie.append(movie)
    
    return searched_movie

@router.get("/search/movie/language/{movie_language}")
def search_movie_by_language(movie_language : str):

    searched_movie = []

    for movie in MovieData:
        if movie_language == movie.language:
            searched_movie.append(movie)
    
    return searched_movie

@router.get("/search/movie/ratings/{movie_ratings}")
def search_movie_by_ratings(movie_ratings : float):

    searched_movie = []

    for movie in MovieData:
        if movie_ratings == movie.ratings:
            searched_movie.append(movie)
    
    return searched_movie

@router.get("/search/movie/ott")
def search_movie_by_ott_released(ott : str):
    searched_movie = []

    for movie in MovieData:
        if ott in movie.ott_released:
            searched_movie.append(movie)
    
    return searched_movie

@router.get("/search/stars")
def search_stars(starcast_name : str):
    searched_movie = []

    for movie in MovieData:
        for starcast in movie.star_casts:

            name = starcast.fname + starcast.lname

            if starcast_name in name:
                searched_movie.append(movie)
    
    return searched_movie

@router.get("/sort/movie/ratings")
def sort_movies_by_ratings(desc : bool = True):

    sorted_movies = sorted(MovieData, key=lambda movie : movie.ratings, reverse=desc)


    return sorted_movies

@router.get("/sort/movie/boxoffice-collection-india")
def sort_movies_by_collection_in_india(desc : bool = True):

    sorted_movies = sorted(MovieData, key=lambda movie : movie.box_office_collection_india, reverse=desc)


    return sorted_movies

@router.get("/sort/movie/boxoffice-collection-worldwide")
def sort_movies_by_collection_in_worldwide(desc : bool = True):

    sorted_movies = sorted(MovieData, key=lambda movie : movie.box_office_collection_worldwide, reverse=desc)


    return sorted_movies

@router.get("/movie/random")
def get_random_movie():
    
    rand_index = random.randint(0, len(MovieData) - 1)

    return MovieData[rand_index]