from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select, SQLModel
from typing import List
from contextlib import asynccontextmanager

# import db model and engine from models.py
from models import TrainTrip, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(title="PKP Tracker API", lifespan=lifespan)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change to exact site in prod
    allow_credentials=True, # For future logging in prod
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/trips", response_model=TrainTrip)
def create_trip(trip: TrainTrip):
    with Session(engine) as session:
        session.add(trip)
        session.commit()
        session.refresh(trip)
        return trip

@app.get("/trips", response_model=List[TrainTrip])
def read_trips():
    with Session(engine) as session:
        trips = session.exec(select(TrainTrip)).all()
        return trips

@app.delete("/trips/{trip_id}")
def delete_trip(trip_id: int):
    with Session(engine) as session:
        trip = session.get(TrainTrip, trip_id)
        if not trip:
            raise HTTPException(status_code=404, detail="Trip not found")
        session.delete(trip)
        session.commit()
        return {"ok": True}

# Welcome endpoint
@app.get("/")
def root():
    return {"message": "Welcome to PKP Tracker API"}


