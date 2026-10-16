from Connection import ConfigureDB as Db
from rich import print
from rich.console import Console

from Technician import View_Assigned_Tickets as VST
from Technician import Update_Ticket_Status as UTS
from Technician import Add_Resolution_Notes as ARN
from Technician import View_Ticket_History as VTH
from Technician import My_Profile as MP

console = Console()


def TechnicianMenu(user_id):
    while True:
        print("\n[bold cyan]╔══════════════════════════════════╗[/bold cyan]")
        print("[bold cyan]║       🛠️  TECHNICIAN MENU          ║[/bold cyan]")
        print("[bold cyan]╚══════════════════════════════════╝[/bold cyan]")

        ch = int(console.input(
            "[bold blue]"
            "1. View Assigned Tickets\n"
            "2. Update Ticket Status\n"
            "3. Add Resolution Notes\n"
            "4. View Ticket History\n"
            "5. My Profile\n"
            "6. Logout\n"
            "[/bold blue][yellow]Enter Your Choice :- [/yellow]"
        ))
        match ch:
            case 1:
                VST.View_Assigned_Tickets(user_id)

            case 2:
                 UTS.Update_Ticket_Status(user_id)

            case 3:
                ARN.Add_Resolution_Notes(user_id)

            case 4:
                VTH.View_Ticket_History(user_id)

            case 5:
                MP.My_Profile(user_id)

            case 6:
                print("[bold green]Thank you. Logging out...[/bold green]")
                break

            case _:
                print("[bold red]Invalid Choice![/bold red]")