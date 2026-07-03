from pydantic import BaseModel

#The Validation Layer (Pydantic)
class CategoryBase(BaseModel):
    id: int
    name: str