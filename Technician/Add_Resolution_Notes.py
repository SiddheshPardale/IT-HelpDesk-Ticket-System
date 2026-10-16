from Connection import ConfigureDB as Db
from rich import print
from rich.console import Console

console = Console()


def Add_Resolution_Notes(user_id):
    ticket_id = console.input("Enter Ticket ID: ")

    Db.cursor1.execute("""
        SELECT ticket_id
        FROM tickets
        WHERE ticket_id = ? AND assigned_to = ?
    """, (ticket_id, user_id))

    row = Db.cursor1.fetchone()

    if not row:
        print("[bold red]Ticket not found or not assigned to you![/bold red]")
        return

    notes = console.input("Enter Resolution Notes: ")

    Db.cursor1.execute("""
        UPDATE tickets
        SET resolved_at = ?
        WHERE ticket_id = ? AND assigned_to = ?
    """, (notes, ticket_id, user_id))

    Db.conn.commit()

    print("[bold green]Resolution notes saved successfully![/bold green]")