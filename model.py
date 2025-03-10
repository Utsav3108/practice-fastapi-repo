from typing import List

from pydantic import BaseModel
import uuid


class Actor(BaseModel):
    id : int
    fname : str
    lname : str
    dob : str

class MovieDetails(BaseModel):
    name : str
    year_of_release : str
    link_to_thumbnail : str
    ott_released : str
    box_office_collection_india : float
    box_office_collection_worldwide : float
    language : str
    ratings : float

class Movie(MovieDetails):
    star_casts : List[Actor]
