# Import necessary libraries
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from rich.console import Console
from datetime import datetime

# Define the ORM's base class
Base = declarative_base()

# Define the Appointment class
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    patient_age = Column(Integer)
    department = Column(String)
    appointment_time = Column(DateTime)

# Connect to the existing SQLite database
engine = create_engine('sqlite:///hospital_inventory.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a console instance for colorful output
console = Console()

def book_appointment():
    patient_name = input("Enter the patient's name: ")
    patient_age = int(input("Enter the patient's age: "))
    department = input("Enter the department the patient will be visiting: ")
    appointment_time = datetime.now()  # This will set the appointment time to the current time

    appointment = Appointment(patient_name=patient_name, patient_age=patient_age, department=department, appointment_time=appointment_time)
    session.add(appointment)
    session.commit()
    console.print(f"Appointment for [bold blue]{patient_name}[/bold blue] (age {patient_age}) in the [bold blue]{department}[/bold blue] department has been booked successfully at [bold blue]{appointment_time}[/bold blue]!", style="bold green")

# Call the function to book an appointment
book_appointment()
