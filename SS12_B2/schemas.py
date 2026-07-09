from pydantic import BaseModel

class OrderResponse(BaseModel):
    id: int
    customer: str

    class Config:
        from_attributes = True