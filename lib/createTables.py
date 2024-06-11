from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Define the ORM's base class
Base = declarative_base()

# Define the Department class
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    head_doctor = Column(String)
    num_nurses = Column(Integer)
    num_doctors = Column(Integer)

# Connect to the existing SQLite database
engine = create_engine('sqlite:///hospital_inventory.db')

# Create the tables
Base.metadata.create_all(engine)
