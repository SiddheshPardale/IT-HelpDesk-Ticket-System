
from Connection import ConfigureDB as Db
from Admin.ExportExcel import ExportExcel
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()


def Manage_Users():
    headers = [
        "user_id",
        "name",
        "email",
        "role",
        "is_verified",
        "is_active",
        "specialization",
        "created_at"
    ]

    query = """
        SELECT user_id, name, email, role, is_verified,
               is_active, specialization, created_at
        FROM users
    """

    Db.cursor1.execute(query)
    rows = Db.cursor1.fetchall()

    if not rows:
        console.print("[yellow]No users found.[/yellow]")
        return

    table = Table(title="User Accounts")

    for header in headers:
        table.add_column(header, overflow="ellipsis", max_width=25)

    for row in rows:
        table.add_row(*[
            Text(str(value) if value is not None else "-")
            for value in row
        ])

    console.print(table)

    console.print("\n[bold cyan]1.[/bold cyan] Activate/Deactivate User")
    console.print("[bold cyan]2.[/bold cyan] Change User Role")
    console.print("[bold cyan]3.[/bold cyan] Export Users")
    console.print("[bold cyan]4.[/bold cyan] Back")

    choice = console.input("Enter choice: ").strip()

    match choice:
        case "1":
            try:
                user_id = int(console.input("Enter User ID: "))

                Db.cursor1.execute(
                    "SELECT is_active, role FROM users WHERE user_id = ?",
                    (user_id,)
                )
                user = Db.cursor1.fetchone()

                if not user:
                    console.print("[red]User not found.[/red]")
                    return

                if user[1] == "ADMIN":
                    console.print("[red]Admin accounts cannot be changed here.[/red]")
                    return

                new_status = 0 if user[0] else 1

                Db.cursor1.execute(
                    "UPDATE users SET is_active = ? WHERE user_id = ?",
                    (new_status, user_id)
                )
                Db.conn.commit()

                console.print("[green]User account status updated.[/green]")

            except ValueError:
                console.print("[red]Enter a valid numeric User ID.[/red]")

        case "2":
            try:
                user_id = int(console.input("Enter User ID: "))
                new_role = console.input(
                    "Enter new role (EMPLOYEE/TECHNICIAN): "
                ).strip().upper()

                if new_role not in ("EMPLOYEE", "TECHNICIAN"):
                    console.print("[red]Invalid role.[/red]")
                    return

                Db.cursor1.execute(
                    "SELECT role FROM users WHERE user_id = ?",
                    (user_id,)
                )
                user = Db.cursor1.fetchone()

                if not user:
                    console.print("[red]User not found.[/red]")
                    return

                if user[0] == "ADMIN":
                    console.print("[red]Admin roles cannot be changed here.[/red]")
                    return

                Db.cursor1.execute(
                    "UPDATE users SET role = ? WHERE user_id = ?",
                    (new_role, user_id)
                )
                Db.conn.commit()

                console.print("[green]User role updated successfully.[/green]")

            except ValueError:
                console.print("[red]Enter a valid numeric User ID.[/red]")

        case "3":
            ExportExcel(
                rows,
                headers,
                "All_Users.xlsx",
                "Users"
            )

        case "4":
            return

        case _:
            console.print("[red]Invalid choice.[/red]")
