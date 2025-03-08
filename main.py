"""

Movie Database API Project.

"""

from fastapi import FastAPI

from typing import List

from model import Movie, Actor
from movie_data import MovieData

import uuid

app = FastAPI()


def publish_movie(movie : Movie):
    movie.id = uuid.uuid4()
    MovieData.append(movie)

    return movie

@app.get("/")
def ping():
    return {
        "message" : "Welcome to Movie Database API Project."
    }



@app.post("/publish")
def publish(movie : Movie):

    movie = publish_movie(movie)

    return {
        "message" : "Movie Successfully published on Movie's Database.",
        "movie" : movie
    }

@app.post("/publish/list")
def publish_list_of_movies(movies : List[Movie]):

    for movie in movies:
        publish_movie(movie)
    
    return {
        "message" : f"{len(movies)} movies successfully published on Movie's Database"
    }



@app.get("/list/movies")
def list_of_movies():
    return MovieData

@app.get("/movie/details")
def get_movie_details_with_id(id : uuid.UUID):

    for movie in MovieData:
        if id == movie.id:
            return movie
        
    return {
        "message" : "No Movie with id specified."
    }



@app.get("/search/movie/name/{movie_name}")
def search_movie_name(movie_name : str):

    searched_movie = []

    for movie in MovieData:
        if movie_name in movie.name:
            searched_movie.append(movie)
    
    return searched_movie

@app.get("/search/movie/year")
def search_movie_by_year(start_year : str, end_year : str):

    searched_movie = []



    for movie in MovieData:

        release_year = movie.year_of_release

        if (start_year <= release_year) and (end_year >= release_year):
            searched_movie.append(movie)
    
    return searched_movie

@app.get("/search/movie/language/{movie_language}")
def search_movie_by_language(movie_language : str):

    searched_movie = []

    for movie in MovieData:
        if movie_language == movie.language:
            searched_movie.append(movie)
    
    return searched_movie

@app.get("/search/movie/ratings/{movie_ratings}")
def search_movie_by_ratings(movie_ratings : int):

    searched_movie = []

    for movie in MovieData:
        if movie_ratings == movie.ratings:
            searched_movie.append(movie)
    
    return searched_movie