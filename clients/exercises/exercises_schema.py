from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class ExercisesSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    course_id: str  = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class Course(BaseModel):
    id: str

class CreateCourseForExerciseResponse(BaseModel):
    course: Course

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновление упражнения.
    """
    exercise: ExercisesSchema

class GetExercisesResponseSchema(BaseModel):
    """
     Описание структуры ответа на получение списка упражнений.
     """
    courseId: str

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: ExercisesSchema
