from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    order_id: str
    amount: float

class OrderResponse(BaseModel):
    id: int
    order_id: str
    status: str
    amount: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

