from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table
from rich import print

console = Console()


def View_Assigned_Tickets(user_id):
    Db.cursor1.execute("""
        SELECT ticket_id, title, category, priority, status, created_at
        FROM tickets
        WHERE assigned_to = ?
        ORDER BY created_at DESC
    """, (user_id,))

    rows = Db.cursor1.fetchall()

    table = Table(
        title="🛠️  MY ASSIGNED TICKETS",
        style="bright_cyan"
    )

    table.add_column("Ticket ID", style="cyan")
    table.add_column("Title", style="white")
    table.add_column("Category", style="blue")
    table.add_column("Priority", style="yellow")
    table.add_column("Status", style="green")
    table.add_column("Created At", style="magenta")

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

    if not rows:
        print("[yellow]No tickets are currently assigned to you.[/yellow]")