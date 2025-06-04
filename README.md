# 🧘‍♀️ Fitness Studio Booking API

A simple REST API for managing fitness classes and bookings at a fictional fitness studio. Built with **FastAPI** and **SQLite**, this app allows users to view upcoming classes, book a spot, and check their bookings.

---

## 🚀 Features

- View all upcoming fitness classes (`GET /classes`)
- Book a class (`POST /book`)
- Retrieve bookings by email (`GET /bookings?email=...`)
- Handle overbooking and input validation
- Timezone-aware: all class timings are stored and served in **IST (Indian Standard Time)**

---

## ⚙️ Tech Stack

- **Backend:** FastAPI
- **Database:** SQLite (with SQLAlchemy ORM)
- **Language:** Python 3.8+
- **Environment:** Lightweight, no external DB required

---

### 🧪 Seeding the Database

To add sample data for testing:

```bash
python seed.py


## 📦 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fitness-studio-booking-api.git
   cd fitness-studio-booking-api


2.Create virtual environment and activate it:
    python -m venv venv
    cd venv/bin/activate 

3.Install dependencies:
    pip install -r requirements.txt

4.Run the API server:
    uvicorn main:app --reload
    
The API will be available at: http://127.0.0.1:8000