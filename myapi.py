from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# students = {
#     1: {
#         "name": "John",
#         "age": 17,
#         "year": "year 12",
#     }
# }
#
# class Student(BaseModel):
#     name: str
#     age: int
#     class_: str


@app.get("/")
async def index():
    return {"data": {"name": "John"}}




