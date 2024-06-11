from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from rich.console import Console

# Define the ORM's base class
Base = declarative_base()

# Define the Doctor class
class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)
    department = Column(String)

# Connect to the existing SQLite database
engine = create_engine('sqlite:///hospital_inventory.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

console = Console()

def add_doctor():
    name = input("Enter the doctor's name: ")
    age = int(input("Enter the doctor's age: "))
    address = input("Enter the doctor's address: ")
    department = input("Enter the doctor's department of specialization: ")

    doctor = Doctor(name=name, age=age, address=address, department=department)
    session.add(doctor)
    session.commit()
    console.print(f"Doctor [bold blue]{name}[/bold blue] added successfully!")

# Call the function to add a doctor
add_doctor()