from pydantic import BaseModel

class CaliforniaHouse(BaseModel):
    id: int
    longitude: float
    latitude: float
    houseage: float
    averooms: float
    avebedrms: float
    population: float
    aveoccup: float
    medinc: float
    medhouseval: float

    class Config:
        from_attributes = True  # 변경된 부분

class Iris(BaseModel):
    id: int
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    target: int

    class Config:
        from_attributes = True  # 변경된 부분
