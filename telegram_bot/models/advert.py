from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class Advert(BaseModel):
    advert_id: str
    courier_id: int
    departure_city: str
    destination_city: str
    departure_date: str
    available_weight: float
    available_volume: float
    price: float
    payment_method: str
    comment: str
    status: str
    created_at: str
    updated_at: str
    responses: List[str]
    is_deleted: bool