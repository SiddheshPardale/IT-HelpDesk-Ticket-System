from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table
console = Console()

def Track_Ticket_Status(user_id):
    while True:
        ch=int(console.input("[bold blue]1.Get the current ticket status\n2.Get the ticket history\n3.Exit[/bold blue]\n[yellow]Enter Your Choice :-[/yellow]"))
        match ch:
            case 1:
                ticket_id = input("Enter Ticket ID: ")
                Db.cursor1.execute("SELECT ticket_id, title, status, assigned_to, created_at, resolved_at FROM tickets WHERE ticket_id = ? AND user_id = ?",(ticket_id,user_id))
                rows = Db.cursor1.fetchone()
    
                table = Table(title="My Ticket Details",style="bright_cyan")
            
                table.add_column("Ticket ID", style="cyan")
                table.add_column("Title", style="green")
                table.add_column("Status", style="blue")
                table.add_column("Assigned To", style="magenta")
                table.add_column("Created at", style="bright_green")
                table.add_column("Resolved at", style="bright_blue")
            
                for i in rows:
                    table.add_row(
                        str(i[0]),
                        str(i[1]),
                        str(i[2]),
                        str(i[3]),
                        str(i[4]),
                        # str(i[5])
                    )
                console.print(table)
            case 2:
                ticket_id = input("Enter Ticket ID: ")
                Db.cursor1.execute("SELECT * FROM ticket_history WHERE ticket_id = ? ORDER BY changed_at ASC;",(ticket_id,))
                rows = Db.cursor1.fetchall()
    
                table = Table(title=" Ticket History ",style="bright_cyan")
            
                table.add_column("Ticket History ID", style="cyan")
                table.add_column("Ticket ID", style="cyan")
                table.add_column("Changed By", style="magenta")
                table.add_column("Old Status", style="blue")
                table.add_column("New Status", style="blue")
                table.add_column("Changed at", style="bright_green")
            
                for i in rows:
                    table.add_row(
                        str(i[0]),
                        str(i[1]),
                        str(i[2]),
                        str(i[3]),
                        str(i[4]),
                        str(i[5])
                    )
                console.print(table)
            case 3:
                    print("Thank You...")
                    break
                    
                        
                        
                

            
    