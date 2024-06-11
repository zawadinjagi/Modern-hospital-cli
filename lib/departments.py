from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
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

def add_department():
    name = input("Enter the department name: ")
    head_doctor = input("Enter the head doctor's name: ")
    num_nurses = int(input("Enter the number of nurses: "))
    num_doctors = int(input("Enter the number of doctors: "))

    department = Department(name=name, head_doctor=head_doctor, num_nurses=num_nurses, num_doctors=num_doctors)
    session.add(department)
    session.commit()
    console.print(f"Department [bold magenta]{name}[/bold magenta] added successfully!", style="bold green")

def view_departments():
    departments = session.query(Department).all()
    table = Table(title="Departments")

    table.add_column("Name", style="cyan")
    table.add_column("Head Doctor", style="magenta")
    table.add_column("Number of Nurses", style="green")
    table.add_column("Number of Doctors", style="yellow")

    for department in departments:
        table.add_row(department.name, department.head_doctor, str(department.num_nurses), str(department.num_doctors))

    console.print(table)

# Example usage
if __name__ == "__main__":
    while True:
        console.print("[bold blue]1.[/bold blue] Add Department", style="bold")
        console.print("[bold blue]2.[/bold blue] View Departments", style="bold")
        console.print("[bold blue]0.[/bold blue] Go back to Menu", style="bold")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_department()
        elif choice == '2':
            view_departments()
        elif choice == '0':
            break
        else:
            console.print("[bold red]Invalid choice. Please try again.[/bold red]")
