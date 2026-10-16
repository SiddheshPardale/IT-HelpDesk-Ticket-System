
from Connection import ConfigureDB as Db
from Admin.ExportExcel import ExportExcel
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()


def View_Email_Logs():
    Db.cursor1.execute(
        "PRAGMA table_info(email_logs)"
    )
    columns = Db.cursor1.fetchall()
    headers = [column[1] for column in columns]

    if not headers:
        console.print("[yellow]Email logs table not found.[/yellow]")
        return

    Db.cursor1.execute("SELECT * FROM email_logs")
    rows = Db.cursor1.fetchall()

    if not rows:
        console.print("[yellow]No email logs found.[/yellow]")
        return

    table = Table(title="Email Logs")

    for header in headers:
        table.add_column(
            header,
            overflow="ellipsis",
            max_width=22
        )

    for row in rows:
        table.add_row(
            *[
                Text(str(value) if value is not None else "-")
                for value in row
            ]
        )

    console.print(table)

    choice = console.input(
        "Export email logs to Excel? (Y/N): "
    ).strip().upper()

    if choice == "Y":
        ExportExcel(
            rows,
            headers,
            "Email_Logs.xlsx",
            "Email Logs"
        )
