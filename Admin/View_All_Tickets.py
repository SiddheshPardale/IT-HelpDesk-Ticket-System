
from Connection import ConfigureDB as Db
from Admin.ExportExcel import ExportExcel
from rich.console import Console
from rich.table import Table

console = Console()


def View_All_Tickets():
    Db.cursor1.execute("SELECT * FROM tickets")
    rows = Db.cursor1.fetchall()

    if not rows:
        console.print("[yellow]No tickets available.[/yellow]")
        return

    headers = [
        column[1]
        for column in Db.cursor1.execute(
            "PRAGMA table_info(tickets)"
        ).fetchall()
    ]

    table = Table(title="All Helpdesk Tickets", style="bright_cyan")

    for header in headers:
        table.add_column(header, overflow="fold")

    for row in rows:
        table.add_row(*[
            str(value) if value is not None else "-"
            for value in row
        ])

    console.print(table)

    while True:
        choice = console.input(
            "\n[bold yellow]Export tickets to Excel? (Y/N): [/bold yellow]"
        ).strip().upper()

        match choice:
            case "Y":
                ExportExcel(
                    rows,
                    headers,
                    "All_Tickets.xlsx",
                    "All Tickets"
                )
                break

            case "N":
                console.print("[cyan]Returning without exporting.[/cyan]")
                break

            case _:
                console.print("[red]Please enter Y or N.[/red]")
