
from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()


def My_Profile(admin_id):
    Db.cursor1.execute("""
        SELECT user_id, name, email, role, is_verified,
               is_active, specialization, created_at
        FROM users
        WHERE user_id = ? AND role = 'ADMIN'
    """, (admin_id,))

    admin = Db.cursor1.fetchone()

    if not admin:
        console.print("[red]Admin profile not found.[/red]")
        return

    headers = [
        "User ID",
        "Name",
        "Email",
        "Role",
        "Verified",
        "Active",
        "Specialization",
        "Created At"
    ]

    table = Table(title="Admin Profile")

    for header in headers:
        table.add_column(header, overflow="ellipsis", max_width=22)

    table.add_row(
        *[
            Text(str(value) if value is not None else "-")
            for value in admin
        ]
    )

    console.print(table)
