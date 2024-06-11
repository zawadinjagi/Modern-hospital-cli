# Import necessary libraries
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from rich.console import Console
from rich.table import Table

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

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create a console instance for colorful output
console = Console()

def view_departments():
    departments = session.query(Department).all()
    table = Table(title="Available Departments")

    table.add_column("Name", style="cyan")
    table.add_column("Head Doctor", style="magenta")
    table.add_column("Number of Nurses", style="green")
    table.add_column("Number of Doctors", style="yellow")

    for department in departments:
        table.add_row(department.name, department.head_doctor, str(department.num_nurses), str(department.num_doctors))

    console.print(table)

# Call the function to view departments
view_departments()
