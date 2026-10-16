from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table

console = Console()

#-------------------------------------
#inserting the data 

def View_My_Ticket_(user_id):
    
    Db.cursor1.execute("SELECT * FROM tickets WHERE user_id= ?", ( user_id, ))
    rows = Db.cursor1.fetchall()


    table = Table(title="My Ticket Details",style="bright_cyan")

    table.add_column("Ticket ID", style="cyan")
    table.add_column("User ID", style="cyan")
    table.add_column("Category", style="green")
    table.add_column("Title", style="green")
    table.add_column("Description", style="yellow")
    table.add_column("Priority", style="blue")
    table.add_column("Status", style="blue")
    table.add_column("Assigned To", style="magenta")
    table.add_column("Created at", style="cyan")
    table.add_column("SLA Deadline", style="bright_blue")
    table.add_column("Resolved at", style="bright_green")
    table.add_column("Closed at", style="bright_blue")

    for i in rows:
        table.add_row(
            str(i[0]),
            str(i[1]),
            str(i[2]),
            str(i[3]),
            str(i[4]),
            str(i[5]),
            str(i[6]),
            str(i[7]),
            str(i[8]),
            str(i[9]),
            str(i[10]),
            str(i[11])
        )

    console.print(table)
    
    Db.conn.commit()