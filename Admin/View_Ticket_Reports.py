from Connection import ConfigureDB as Db
from Admin.ExportExcel import ExportExcel
from rich.console import Console
from rich.table import Table

console = Console()


def View_Ticket_Reports():
    Db.cursor1.execute("SELECT * FROM tickets")
    rows = Db.cursor1.fetchall()

    if not rows:
        console.print("[yellow]No tickets available for reports.[/yellow]")
        return

    headers = [
        column[1] for column in
        Db.cursor1.execute("PRAGMA table_info(tickets)").fetchall()
    ]

    if "status" in headers:
        Db.cursor1.execute("""
            SELECT status, COUNT(*)
            FROM tickets
            GROUP BY status
        """)
        summary = Db.cursor1.fetchall()

        table = Table(title="Ticket Status Summary")
        table.add_column("Status")
        table.add_column("Total Tickets", justify="right")

        for status, count in summary:
            table.add_row(str(status or "Unknown"), str(count))

        console.print(table)
    else:
        console.print(
            "[yellow]Status summary unavailable: no status column found.[/yellow]"
        )

    detail_table = Table(title="Detailed Ticket Report")
    for header in headers:
        detail_table.add_column(header, overflow="fold")

    for row in rows:
        detail_table.add_row(*[
            str(value) if value is not None else "-"
            for value in row
        ])

    console.print(detail_table)

    while True:
        choice = console.input(
            "Export detailed ticket report to Excel? (Y/N): "
        ).strip().upper()

        match choice:
            case "Y":
                ExportExcel(
                    rows,
                    headers,
                    "Ticket_Reports.xlsx",
                    "Ticket Reports"
                )
                break
            case "N":
                break
            case _:
                console.print("[red]Enter Y or N.[/red]")