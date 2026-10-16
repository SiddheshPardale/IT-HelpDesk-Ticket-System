from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table
console = Console()

def Add_Comments(user_id):
    while True:
        ch=int(console.input("[bold blue]1.Save a comment\n2.Display comments for a ticket\n3.Exit[/bold blue]\n[yellow]Enter Your Choice :-[/yellow]"))
        match ch:
            case 1:
                ticket_id = input("Enter Ticket ID: ")
                comment = input("Enter Comment: ")
                Db.cursor1.execute("INSERT INTO ticket_comments (ticket_id, user_id, comment) VALUES (?, ?, ?)",(ticket_id,user_id,comment))
                Db.conn.commit()
                print("Comment Inserted!")
            case 2:
                ticket_id = input("Enter Ticket ID: ")
                Db.cursor1.execute("SELECT tc.*, u.name FROM ticket_comments AS tc JOIN users AS u ON tc.user_id = u.user_id WHERE tc.ticket_id = ? ORDER BY tc.created_at ASC;",(ticket_id,))
                rows = Db.cursor1.fetchall()


                table = Table(title="Display comments for a ticket ",style="bright_cyan")
            
                table.add_column("Ticket Comment ID", style="cyan")
                table.add_column("Ticket ID", style="cyan")
                table.add_column("User ID", style="magenta")
                table.add_column("User Name", style="blue")
                table.add_column("Comments ", style="blue")
                table.add_column("Changed at", style="bright_green")

            
                for i in rows:
                    table.add_row(
                        str(i[0]),
                        str(i[1]),
                        str(i[2]),
                        str(i[5]),
                        str(i[3]),
                        str(i[4])
                    )
                console.print(table)
                
            case 3:
                print("Thank You...")
                break
                    
                        
                        
                

            
    