# from Connection import ConfigureDB as Db
from Employee import Create_Ticket as CT
from Employee import ViewTicket as VT
from Employee import Add_Comments as AC
from Employee import Track_Ticket_Status as TTS
from Employee import My_Profile as MP
from rich import print
from rich.console import Console
console = Console()

def EmployeeMenu(user_id):
    while True:
        print("=================================================================")
        print("\t\t[bold cyan]╔══════════════════════════════╗[/bold cyan]")
        print("\t\t[bold cyan]║       👤 EMPLOYEE MENU       ║[/bold cyan]")
        print("\t\t[bold cyan]╚══════════════════════════════╝[/bold cyan]")
        print("=================================================================")
        ch=int(console.input("[bold blue]1.Create ticket\n2.View my tickets\n3.Track ticket status\n4.Add comments\n5.My profile\n6.Logout[/bold blue]\n[yellow]Enter Your Choice :-[/yellow]"))
        
        match ch:
            case 1:
                CT.CreateTicket(user_id)
            case 2:
                VT.View_My_Ticket_(user_id)
            case 3:
                TTS.Track_Ticket_Status(user_id)
            case 4:
                AC.Add_Comments(user_id)
            case 5:
                MP.My_Profile(user_id)
            case 6:
                print("Thank You See U Again.......")
                break
            case _:
                    print("Invalid Choice !....")