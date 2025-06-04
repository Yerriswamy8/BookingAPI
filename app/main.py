from fastapi import FastAPI, Depends, HTTPException, Query  # type: ignore
from sqlalchemy.orm import Session  # type: ignore
from app import models, schemas, crud
from app.database import engine, SessionLocal
from app.seed import seed_classes
from fastapi.middleware.cors import CORSMiddleware  # type: ignore
from typing import List
from app.routes import booking_routes 


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(booking_routes.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    seed_classes(db)
    db.close()

# Endpoint to fetch available classes
@app.get("/classes", response_model=List[schemas.ClassOut])
def get_classes(db: Session = Depends(get_db)):
    return crud.get_classes(db)

# Endpoint to fetch bookings by email
@app.get("/bookings", response_model=List[schemas.BookingOut])
def get_bookings(email: str = Query(...), db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, email)
