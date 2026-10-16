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
                print("[bold green]Login successful![/bold green]")
                print(f"\n[bold green]Welcome: {Login1["name"]}![/bold green]")
                print(f"[bold green]Role: {Login1["role"]}[/bold green]")

            if Login1["role"] == "EMPLOYEE":
                Employee.EmployeeMenu(Login1["user_id"])
                break
            elif Login1["role"] == "TECHNICIAN":
                Technician.TechnicianMenu(Login1["user_id"])
                break
            elif Login1["role"] == "ADMIN":
                Admin.AdminMenu(Login1["user_id"])
                break
            else:
                print("Create Account With Correct Role ")
                break

        case 3:
            print("Thank You....")
            break
        case _:
            print("Invalid Choice !....")