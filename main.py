from Connection import ConfigureDB as Db
from Employee import EmployeeMenu as Employee
from Technician import TechnicianMenu as Technician
from Admin import AdminMenu as Admin
from Connection import user as user
from Connection import Login as Login
from rich import print
from rich.console import Console
console = Console()

while True:
    print("=============================================================")
    print("\t\t[bright_cyan]IT HelpDesk Ticket System [/bright_cyan]")
    print("=============================================================")
    ch=int(console.input("[bold blue]1.Register\n2.Login\n3.Exit[/bold blue]\n[yellow]Enter Your Choice :-[/yellow]"))
    
    match ch:
        case 1:
            user.RegisterUser()
        case 2:
            Login1 = Login.Login()
    
            if Login1:
                role = Login1.get("role")
                print("[bold green]Login successful![/bold green]")
                print(f"\n[bold green]Welcome: {Login1["name"]}![/bold green]")
                print(f"[bold green]Role: {Login1["role"]}[/bold green]")

                if role == "EMPLOYEE":
                    Employee.EmployeeMenu(Login1["user_id"])
                    break
                elif role == "TECHNICIAN":
                    Technician.TechnicianMenu(Login1["user_id"])
                    break
                elif role == "ADMIN":
                    Admin.AdminMenu(Login1["user_id"])
                    break
                else:
                    console.print("[red]Invalid or unrecognized user role.[/red]")
            else:
                console.print("[red]Login failed. Please check your credentials and try again.[/red]")

        case 3:
            print("Thank You....")
            break
        case _:
            print("Invalid Choice !....")
