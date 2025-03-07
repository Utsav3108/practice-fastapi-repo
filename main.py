"""

Movie Database API Project.

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ping():
    return {
        "message" : "Welcome to Movie Database API Project."
    }