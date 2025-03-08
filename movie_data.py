from typing import List

from model import Movie


MovieData : List[Movie] = []

"""
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Inception",
    "year_of_release": "2010",
    "link_to_Thumbnail": "string",
    "ott_released": "Netflix, Prime",
    "box_office_collection_india": 15000000,
    "box_office_collection_worldwide": 829895144,
    "star_casts": [
      {
        "id": 0,
        "fname": "Leonardo",
        "lname": "DiCaprio",
        "dob": "11/11/1974"
      }
    ],
    "language": "English",
    "ratings": 2
  },
  {
    "id": "c0a80101-7654-4b3d-a9c8-87f4c91baf77",
    "name": "The Dark Knight",
    "year_of_release": "2008",
    "link_to_Thumbnail": "string",
    "ott_released": "HBO Max, Prime",
    "box_office_collection_india": 18000000,
    "box_office_collection_worldwide": 1004558444,
    "star_casts": [
      {
        "id": 0,
        "fname": "Christian",
        "lname": "Bale",
        "dob": "30/01/1974"
      }
    ],
    "language": "English",
    "ratings": 2
  },
  {
    "id": "c69d5d6b-1a4f-4b97-bc72-72a7fcd85d66",
    "name": "Interstellar",
    "year_of_release": "2014",
    "link_to_Thumbnail": "string",
    "ott_released": "Netflix",
    "box_office_collection_india": 22000000,
    "box_office_collection_worldwide": 677471339,
    "star_casts": [
      {
        "id": 0,
        "fname": "Matthew",
        "lname": "McConaughey",
        "dob": "04/11/1969"
      }
    ],
    "language": "English",
    "ratings": 5
  },
  {
    "id": "5b8db640-2b74-11eb-adc1-0242ac120002",
    "name": "Avengers: Endgame",
    "year_of_release": "2019",
    "link_to_Thumbnail": "string",
    "ott_released": "Disney+",
    "box_office_collection_india": 373000000,
    "box_office_collection_worldwide": 2797800564,
    "star_casts": [
      {
        "id": 0,
        "fname": "Robert",
        "lname": "Downey Jr.",
        "dob": "04/04/1965"
      }
    ],
    "language": "English",
    "ratings": 5
  },
  {
    "id": "7f31f074-2b74-11eb-adc1-0242ac120002",
    "name": "Titanic",
    "year_of_release": "1997",
    "link_to_Thumbnail": "string",
    "ott_released": "Prime, Disney+",
    "box_office_collection_india": 25000000,
    "box_office_collection_worldwide": 2201647264,
    "star_casts": [
      {
        "id": 0,
        "fname": "Kate",
        "lname": "Winslet",
        "dob": "05/10/1975"
      }
    ],
    "language": "English",
    "ratings": 3
  },
  {
    "id": "8f9d68e2-2b74-11eb-adc1-0242ac120002",
    "name": "3 Idiots",
    "year_of_release": "2009",
    "link_to_Thumbnail": "string",
    "ott_released": "Netflix, Prime",
    "box_office_collection_india": 202000000,
    "box_office_collection_worldwide": 460000000,
    "star_casts": [
      {
        "id": 0,
        "fname": "Aamir",
        "lname": "Khan",
        "dob": "14/03/1965"
      }
    ],
    "language": "Hindi",
    "ratings": 1
  },
  {
    "id": "a19c2364-2b74-11eb-adc1-0242ac120002",
    "name": "Dangal",
    "year_of_release": "2016",
    "link_to_Thumbnail": "string",
    "ott_released": "Disney+",
    "box_office_collection_india": 387000000,
    "box_office_collection_worldwide": 2008000000,
    "star_casts": [
      {
        "id": 0,
        "fname": "Aamir",
        "lname": "Khan",
        "dob": "14/03/1965"
      }
    ],
    "language": "Hindi",
    "ratings": 2
  },
  {
    "id": "b3de75a6-2b74-11eb-adc1-0242ac120002",
    "name": "Sholay",
    "year_of_release": "1975",
    "link_to_Thumbnail": "string",
    "ott_released": "Prime",
    "box_office_collection_india": 15000000,
    "box_office_collection_worldwide": 30000000,
    "star_casts": [
      {
        "id": 0,
        "fname": "Amitabh",
        "lname": "Bachchan",
        "dob": "11/10/1942"
      }
    ],
    "language": "Hindi",
    "ratings": 1
  },
  {
    "id": "c6a73db4-2b74-11eb-adc1-0242ac120002",
    "name": "Baahubali 2: The Conclusion",
    "year_of_release": "2017",
    "link_to_Thumbnail": "string",
    "ott_released": "Netflix, Prime",
    "box_office_collection_india": 510000000,
    "box_office_collection_worldwide": 1810000000,
    "star_casts": [
      {
        "id": 0,
        "fname": "Prabhas",
        "lname": "Raju",
        "dob": "23/10/1979"
      }
    ],
    "language": "Telugu",
    "ratings": 4
  },
  {
    "id": "d91f34a8-2b74-11eb-adc1-0242ac120002",
    "name": "KGF: Chapter 2",
    "year_of_release": "2022",
    "link_to_Thumbnail": "string",
    "ott_released": "Prime",
    "box_office_collection_india": 850000000,
    "box_office_collection_worldwide": 1250000000,
    "star_casts": [
      {
        "id": 0,
        "fname": "Yash",
        "lname": "Gowda",
        "dob": "08/01/1986"
      }
    ],
    "language": "Kannada",
    "ratings": 3
  }
]

"""