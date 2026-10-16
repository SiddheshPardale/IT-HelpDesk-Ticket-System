from Connection import ConfigureDB as Db
from Admin.ExportExcel import ExportExcel
from rich.console import Console
from rich.table import Table

console = Console()


def Assign_Ticket():
    Db.cursor1.execute("""
        SELECT ticket_id, assigned_to
        FROM tickets
    """)
    ticket_rows = Db.cursor1.fetchall()

    Db.cursor1.execute("""
        SELECT user_id, name, email
        FROM users
        WHERE role = 'TECHNICIAN' AND is_active = 1
    """)
    technicians = Db.cursor1.fetchall()

    if not ticket_rows:
        console.print("[yellow]No tickets available.[/yellow]")
        return

    if not technicians:
        console.print("[yellow]No active technicians available.[/yellow]")
        return

    Db.cursor1.execute("SELECT * FROM tickets")
    all_tickets = Db.cursor1.fetchall()
    ticket_headers = [
        column[1] for column in
        Db.cursor1.execute("PRAGMA table_info(tickets)").fetchall()
    ]

    table = Table(title="Tickets")
    for header in ticket_headers:
        table.add_column(header, overflow="fold")
    for row in all_tickets:
        table.add_row(*[
            str(value) if value is not None else "-"
            for value in row
        ])
    console.print(table)

    tech_table = Table(title="Active Technicians")
    tech_table.add_column("User ID")
    tech_table.add_column("Name")
    tech_table.add_column("Email")

    for tech in technicians:
        tech_table.add_row(str(tech[0]), str(tech[1]), str(tech[2]))

    console.print(tech_table)

    try:
        ticket_id = console.input("Enter Ticket ID to assign: ")
        technician_id = int(console.input("Enter Technician User ID: "))

        if not any(row[0] == ticket_id for row in ticket_rows):
            console.print("[red]Ticket ID not found.[/red]")
            return

        if not any(row[0] == technician_id for row in technicians):
            console.print("[red]Active technician ID not found.[/red]")
            return

        Db.cursor1.execute("""
            UPDATE tickets
            SET assigned_to = ?
            WHERE ticket_id = ?
        """, (technician_id, ticket_id))

        Db.conn.commit()
        console.print("[green]Ticket assigned successfully.[/green]")

    except ValueError:
        console.print("[red]Enter valid  IDs.[/red]")
        return

    Db.cursor1.execute("SELECT * FROM tickets")
    rows = Db.cursor1.fetchall()
    headers = [
        column[1] for column in
        Db.cursor1.execute("PRAGMA table_info(tickets)").fetchall()
    ]

    while True:
        choice = console.input("Export tickets to Excel? (Y/N): ").strip().upper()

        match choice:
            case "Y":
                ExportExcel(rows, headers, "All_Tickets.xlsx", "All Tickets")
                break
            case "N":
                break
            case _:
                console.print("[red]Enter Y or N.[/red]")