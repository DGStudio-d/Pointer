from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.models.sql_models import OrderStatus

class OrderItemBase(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderItemCreate(BaseModel):
    product_id: str
    quantity: int

class OrderItemResponse(OrderItemBase):
    id: str
    
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    delivery_address_id: str
    notes: Optional[str] = None

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderResponse(OrderBase):
    id: str
    user_id: str
    driver_id: Optional[str] = None
    status: OrderStatus
    total_amount: float
    delivery_fee: float
    created_at: datetime
    updated_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    order_items: List[OrderItemResponse] = []
    
    class Config:
        from_attributes = True
