# Import necessary libraries
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from rich.console import Console
from rich.table import Table

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

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a console instance for colorful output
console = Console()

def view_appointments():
    appointments = session.query(Appointment).all()
    table = Table(title="Booked Appointments")

    table.add_column("Patient Name", style="cyan")
    table.add_column("Patient Age", style="magenta")
    table.add_column("Department", style="green")
    table.add_column("Appointment Time", style="yellow")

    for appointment in appointments:
        table.add_row(appointment.patient_name, str(appointment.patient_age), appointment.department, str(appointment.appointment_time))

    console.print(table)

# Call the function to view appointments
view_appointments()
