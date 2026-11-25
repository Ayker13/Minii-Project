from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI(

    title="Student Performance API",

    version="1.0.0"

)


class StudentInput(BaseModel):

    study_hours: float

    attendance: float

    previous_score: float

    assignments_completed: int


@app.get("/")

def home():

    return {"message": "Student Performance API is running"}


@app.post("/predict")

