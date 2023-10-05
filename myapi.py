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

@app.get("/get-student/{student_id}")
async def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0, le=3)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
async def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}



