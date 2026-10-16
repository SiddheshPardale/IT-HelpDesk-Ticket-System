
from rich import print
from rich.console import Console

from Admin import View_All_Tickets as VAT
from Admin import Assign_Ticket as AT
from Admin import Manage_User_Account as MUA
from Admin import View_Ticket_Reports as VTR
from Admin import View_Email_Logs as VEL
from Admin import My_Profile as MP

console = Console()


def AdminMenu(user_id):
    while True:
        print("\n[bold cyan]╔══════════════════════════════════════╗[/bold cyan]")
        print("[bold cyan]║           ⚙️ ADMIN MENU              ║[/bold cyan]")
        print("[bold cyan]╚══════════════════════════════════════╝[/bold cyan]")

        try:
            ch = int(console.input(
                "[bold blue]"
                "1. View All Tickets\n"
                "2. Assign Ticket to Technician\n"
                "3. Manage User Accounts\n"
                "4. View Ticket Reports\n"
                "5. View Email Logs\n"
                "6. My Profile\n"
                "7. Logout\n"
                "[/bold blue][yellow]Enter Your Choice: [/yellow]"
            ))
        except ValueError:
            print("[bold red]Please enter a valid number![/bold red]")
            continue

        match ch:
            case 1:
                VAT.View_All_Tickets()
            case 2:
                AT.Assign_Ticket()

            case 3:
                MUA.Manage_Users()

            case 4:
                VTR.View_Ticket_Reports()

            case 5:
                VEL.View_Email_Logs()

            case 6:
                MP.My_Profile(user_id)

            case 7:
                print("[bold green]Admin logged out successfully![/bold green]")
                break

            case _:
                print("[bold red]Invalid Choice![/bold red]")
