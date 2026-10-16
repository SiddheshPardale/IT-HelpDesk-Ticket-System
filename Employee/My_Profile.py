from Connection import ConfigureDB as Db
from rich.console import Console
from rich.table import Table
from rich import print
from rich import box
console = Console()

def My_Profile(user_id):
    Db.cursor1.execute("SELECT user_id, name, email, role,is_verified, is_active, created_at FROM users WHERE user_id = ?;",(user_id,))
    rows = Db.cursor1.fetchone()
    is_active ="Active Account" 
    if rows[5] != 1:
        is_active = "Not Active Account "
    
    width = 30
    print(f"\t[bold cyan]╔{'═' * width}╗[/bold cyan]")
    print(f"\t[bold green]║{'👤 ' + str(rows[1]):^{width-1}}║[/bold green]")
    print(f"\t[bold cyan]║{'Employee ID: ' + str(rows[0]):^{width}}║[/bold cyan]")
    print(f"\t[bold green]║{str(is_active):^{width}}║[/bold green]")
    print(f"\t[bold cyan]╚{'═' * width}╝[/bold cyan]")

    print("[bold green]----------------------------------------------------[/bold green]")


    print("\t\t[bold cyan]Account Information [/bold cyan]")
    print(f"[bold cyan]✉️  Email Address:[/bold cyan]\n{rows[2]}\n")
    print(f"[bold cyan]🛡️  Role::[/bold cyan]\n{rows[3]}\n")
    print(f"[bold cyan]📅 Registered:[/bold cyan]\n{rows[6]}")


    print("[bold green]----------------------------------------------------[/bold green]")

    Db.cursor1.execute("""
    SELECT
        COUNT(*) AS total_tickets,
        SUM(CASE WHEN status = 'OPEN' THEN 1 ELSE 0 END),
        SUM(CASE WHEN status = 'IN_PROGRESS' THEN 1 ELSE 0 END),
        SUM(CASE WHEN status = 'RESOLVED' THEN 1 ELSE 0 END)
    FROM tickets
    WHERE user_id = ?
    """, (user_id,))
    row1 = Db.cursor1.fetchone()

    summary_table = Table(
    title="🎫 TICKET SUMMARY",
    box=box.ROUNDED,
    border_style="bold cyan",
    header_style="bold cyan",
    show_header=True,
    )

    summary_table.add_column("Category", style="white")
    summary_table.add_column("Count", style="bold")
    
    summary_table.add_row("📋 Total Tickets", f"[bold white]{row1[0]}[/]")
    summary_table.add_row("🔴 Open Tickets", f"[bold red]{row1[1]}[/]")
    summary_table.add_row("🟡 In Progress", f"[bold yellow]{row1[2]}[/]")
    summary_table.add_row("🟢 Resolved", f"[bold green]{row1[3]}[/]")
    
    console.print(summary_table)

    



