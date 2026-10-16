from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table
from rich import print

console = Console()


def View_Ticket_History(user_id):
    ticket_id = console.input("Enter Ticket ID: ")

    Db.cursor1.execute("""
        SELECT ticket_id
        FROM tickets
        WHERE ticket_id = ? AND assigned_to = ?
    """, (ticket_id, user_id))

    if not Db.cursor1.fetchone():
        print("[bold red]Ticket not found or not assigned to you![/bold red]")
        return

    Db.cursor1.execute("""
        SELECT ticket_id, old_status, new_status, changed_by, changed_at
        FROM ticket_history
        WHERE ticket_id = ?
        ORDER BY changed_at ASC
    """, (ticket_id,))

    rows = Db.cursor1.fetchall()

    table = Table(title="📜 TICKET HISTORY", style="bright_cyan")

    table.add_column("Ticket ID", style="cyan")
    table.add_column("Old Status", style="yellow")
    table.add_column("New Status", style="green")
    table.add_column("Changed By", style="magenta")
    table.add_column("Changed At", style="blue")

    for i in rows:
        table.add_row(*(str(value) for value in i))

    console.print(table)

    if not rows:
        print("[yellow]No history found for this ticket.[/yellow]")