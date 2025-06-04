from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from app.database import SessionLocal
from app import crud, schemas
import traceback

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book", response_model=schemas.BookingResponse)
async def book_class(booking: schemas.BookingRequest, db: Session = Depends(get_db)):
    try:
        saved_booking = crud.create_booking(db, booking)
        return {
            "message": f"Class {booking.class_id} successfully booked for {booking.client_email}",
            "booking": saved_booking
        }
    except HTTPException as http_ex:
        raise http_ex 
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Booking failed: {str(e)}")

@router.get("/bookings/{email}", response_model=list[schemas.Booking])
def get_bookings_by_email(email: str, db: Session = Depends(get_db)):
    bookings = crud.get_bookings_by_email(db, email)
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found for this email")
    return bookings

@router.get("/bookings", response_model=list[schemas.Booking])
def get_all_bookings(db: Session = Depends(get_db)):
    bookings = crud.get_all_bookings(db)
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found")
    return bookings