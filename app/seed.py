from sqlalchemy.orm import Session # type: ignore
from app import models
from datetime import datetime, timedelta
import pytz

def seed_classes(db: Session):
    if db.query(models.FitnessClass).first():
        return 

    ist = pytz.timezone("Asia/Kolkata")
    sample_classes = [
        models.FitnessClass(name="Yoga", datetime=ist.localize(datetime.now() + timedelta(days=1)), instructor="Alice", available_slots=30),
        models.FitnessClass(name="Zumba", datetime=ist.localize(datetime.now() + timedelta(days=2)), instructor="Bob", available_slots=30),
        models.FitnessClass(name="HIIT", datetime=ist.localize(datetime.now() + timedelta(days=3)), instructor="Carol", available_slots=30),
    ]
    db.add_all(sample_classes)
    db.commit()
    print("Sample classes seeded successfully.")