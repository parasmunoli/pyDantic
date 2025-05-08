from pydantic import BaseModel #type: ignore
from typing import List

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

class Lesson(BaseModel):
    lessonId: int
    lessonName: str
    topic: str

class Module(BaseModel):
    moduleId: int
    moduleName: str
    description: str
    lessons: List[Lesson]

class Course(BaseModel):
    courseName: str
    description: str
    tutorName: str
    modules: List[Module]

lessons = [
    Lesson(
        lessonId=1,
        lessonName='lesson1',
        topic='Hello World!'
    ),
    Lesson(
        lessonId=2,
        lessonName='lesson2',
        topic='Hello World 2!'
    )
]

modules = [
    Module(
        moduleId=1,
        moduleName='module1',
        description='Introduction Module 1',
        lessons=[lessons[0]]
    ),
    Module(
        moduleId=2,
        moduleName='module2',
        description='Introduction Module 2',
        lessons=[lessons[1]]
    )
]

course = Course(
    courseName='course1',
    description='Hello World!',
    tutorName='admin',
    modules=modules,
)

print(course)