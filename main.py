"""

Movie Database API Project.

"""

from fastapi import FastAPI
from router import router


app = FastAPI()

app.include_router(router=router,tags=["Movie Database Endpoints"])

@app.get("/")
def home():
    return {
        "message" : "Welcome to the home of Movie Database. Got to /docs to visit each endpoints."
    }