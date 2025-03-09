from typing import List

from pydantic import BaseModel
import uuid


class Actor(BaseModel):
    id : int
    fname : str
    lname : str
    dob : str
    


class Movie(BaseModel):
    id : uuid.UUID
    name : str
    year_of_release : str
    link_to_Thumbnail : str
    ott_released : List[str]
    box_office_collection_india : float
    box_office_collection_worldwide : float
    star_casts : List[Actor]
    language : str
    ratings : float
