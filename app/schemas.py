from pydantic import BaseModel, EmailStr # type: ignore
from datetime import datetime

class ClassBase(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class ClassOut(ClassBase):
    id: int
    class Config:
        from_attributes = True

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    class Config:
        from_attributes = True

class BookingResponse(BaseModel):
    message: str
    booking: BookingOut

class Booking(BaseModel):
    id: int
    client_email: str
    class_id: int
    # booking_time: datetime

    class Config:
        from_attributes = True
