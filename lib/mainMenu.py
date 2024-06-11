from rich.console import Console
from rich import print as rprint
import subprocess

console = Console()

def main_menu():
    rprint("[blink][bold blue]Welcome to Rocky Hills Modern Hospital[/bold blue][/blink]")
    email = input("Please enter your email to log in: ")
    rprint(f"[blink][bold red]User {email} logged in successfully[/bold red][/blink]")

    while True:
        console.print("\n1. Book an appointment")
        console.print("2. Input doctor's details")
        console.print("3. Add a new department")
        console.print("4. View all available departments")
        console.print("5. View all booked appointments")
        console.print("00. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            
            subprocess.run(["python", "appointments.py"])
        elif choice == '2':
           
            subprocess.run(["python", "docDetails.py"])
        elif choice == '3':
           
            subprocess.run(["python", "departments.py"])
        elif choice == '4':
            
            subprocess.run(["python", "viewDepartments.py"])
        elif choice == '5':
           
            subprocess.run(["python", "viewAppointments.py"])
        elif choice == '00':
            rprint("[blink][bold red]User logged out. Have a nice day![/bold red][/blink]")
            break
        else:
            console.print("Invalid choice. Please enter a valid option.", style="bold red")

# Call the main menu function
main_menu()
