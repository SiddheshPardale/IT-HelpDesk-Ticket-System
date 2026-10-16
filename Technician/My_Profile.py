from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table
from rich import print

console = Console()


def My_Profile(user_id):
    Db.cursor1.execute("""
        SELECT user_id, name, email, role, is_active, created_at
        FROM users
        WHERE user_id = ?
    """, (user_id,))

    user = Db.cursor1.fetchone()

    if not user:
        print("[bold red]Technician profile not found![/bold red]")
        return

    profile = Table(
        title="\n 🛠️  TECHNICIAN PROFILE",
        style="bright_cyan"
    )

    profile.add_column("Field", style="cyan")
    profile.add_column("Details", style="white")

    profile.add_row("Technician ID", str(user[0]))
    profile.add_row("Name", str(user[1]))
    profile.add_row("Email", str(user[2]))
    profile.add_row("Role", str(user[3]))
    profile.add_row(
        "Account Status",
        "Active" if user[4] else "Inactive"
    )
    profile.add_row("Registered On", str(user[5]))

    console.print(profile)

    Db.cursor1.execute("""
        SELECT
            COUNT(*),
            SUM(CASE WHEN status = 'OPEN' THEN 1 ELSE 0 END),
            SUM(CASE WHEN status = 'IN_PROGRESS' THEN 1 ELSE 0 END),
            SUM(CASE WHEN status = 'RESOLVED' THEN 1 ELSE 0 END)
        FROM tickets
        WHERE assigned_to = ?
    """, (user_id,))

    summary = Db.cursor1.fetchone()

    counts = Table(
        title="🎫 ASSIGNED TICKET SUMMARY",
        style="bright_cyan"
    )

    counts.add_column("Category", style="white")
    counts.add_column("Count", justify="center", style="bold")

    counts.add_row("Total Assigned", str(summary[0] or 0))
    counts.add_row("Open", str(summary[1] or 0))
    counts.add_row("In Progress", str(summary[2] or 0))
    counts.add_row("Resolved", str(summary[3] or 0))

    console.print(counts)