from Connection import ConfigureDB as Db
from rich import print
from rich.console import Console

console = Console()


def Update_Ticket_Status(user_id):
    ticket_id = console.input("Enter Ticket ID: ")

    Db.cursor1.execute("""
        SELECT status
        FROM tickets
        WHERE ticket_id = ? AND assigned_to = ?
    """, (ticket_id, user_id))

    row = Db.cursor1.fetchone()

    if not row:
        print("[bold red]Ticket not found or not assigned to you![/bold red]")
        return

    old_status = row[0]

    print(f"\n[cyan]Current Status: {old_status}[/cyan]")
    print("\n[bold cyan]1. OPEN[/bold cyan]")
    print("[yellow]2. IN_PROGRESS[/yellow]")
    print("[green]3. RESOLVED[/green]")
    print("[blue]4. CLOSED[/blue]")

    ch = int(console.input("Select New Status: "))

    match ch:
        case 1:
            new_status = "OPEN"
        case 2:
            new_status = "IN_PROGRESS"
        case 3:
            new_status = "RESOLVED"
        case 4:
            new_status = "CLOSED"
        case _:
            print("[bold red]Invalid Choice![/bold red]")
            return


    if new_status == "CLOSED":
        Db.cursor1.execute("""
            UPDATE tickets
            SET status = ?, closed_at = CURRENT_TIMESTAMP
            WHERE ticket_id = ? AND assigned_to = ?
        """, (new_status, ticket_id, user_id))

    else:
        Db.cursor1.execute("""
            UPDATE tickets
            SET status = ?
            WHERE ticket_id = ? AND assigned_to = ?
        """, (new_status, ticket_id, user_id))

    Db.conn.commit()

    print(f"[bold green]Ticket status updated to {new_status}![/bold green]")