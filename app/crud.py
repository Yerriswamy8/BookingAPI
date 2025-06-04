from sqlalchemy.orm import Session # type: ignore
from app import models, schemas
from fastapi import HTTPException # type: ignore

def get_classes(db: Session):
    return db.query(models.FitnessClass).all()

def create_booking(db: Session, booking: schemas.BookingRequest):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    fitness_class.available_slots -= 1
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings_by_email(db: Session, email: str):
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()

def get_all_bookings(db: Session):
    return db.query(models.Booking).all()

