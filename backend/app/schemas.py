from pydantic import BaseModel

#The Validation Layer (Pydantic)
class CategoryBase(BaseModel):
    name: str