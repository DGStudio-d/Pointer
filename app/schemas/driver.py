from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DriverBase(BaseModel):
    license_number: str
    vehicle_type: Optional[str] = None
    vehicle_number: Optional[str] = None
    is_available: bool = True

class DriverCreate(DriverBase):
    user_id: str

class DriverResponse(DriverBase):
    id: str
    user_id: str
    rating: float
    total_deliveries: int
    created_at: datetime
    
    class Config:
        from_attributes = True
