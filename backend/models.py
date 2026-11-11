from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field, create_engine

class TrainTrip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_station: str
    end_station: str
    travel_date: Optional[date] = None
    train_type: Optional[str] = None  # example IC or EIP
    rating: Optional[int] = Field(default=None, ge=1, le=5) # Grade 1-5

# SQLite database configuration
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
    print("Database created succesfully")