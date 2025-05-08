from pydantic import BaseModel
from typing import List


# TODO: Create Lesson model here
# Task 1: Define a Lesson model
# - title: str
# - duration: int (in minutes)


# TODO: Create Module model here
# Task 2: Define a Module model
# - title: str
# - lessons: List[Lesson]


# TODO: Create Course model here
# Task 3: Define a Course model
# - title: str
# - description: str
# - modules: List[Module]

class Lesson(BaseModel):
    title: str
    duration: int

class Module(BaseModel):
    title: str
    lessons: List[Lesson]

class Course(BaseModel):
    title: str
    description: str
    modules: List[Module]

course = Course(
    title = "Course 1!",
    description = "Course description",
    modules = [
        Module(
            title = "Module 1!",
            lessons = [
                Lesson(
                    title = "Lesson 1!",
                    duration = 90
                ),
                Lesson(
                    title = "Lesson 2!",
                    duration = 120
                )
            ]
        ),
        Module(
            title = "Module 2!",
            lessons = [
                Lesson(
                    title = "Lesson 3!",
                    duration = 150
                ),
                Lesson(
                    title = "Lesson 4!",
                    duration = 180
                )
            ]
        )
    ]
)

print(course)