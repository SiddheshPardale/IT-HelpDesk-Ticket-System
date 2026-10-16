from Connection import ConfigureDB as Db
from pathlib import Path
from rich.console import Console
from rich import print 
import random as r
from datetime import datetime, timedelta
import bcrypt 
console = Console()


def Login():
    print("\n[bold cyan]========== USER Login ==========[/bold cyan]")
    email = console.input("[yellow]Enter Email:-[/yellow]").strip().lower()
    password = console.input("[yellow]Enter Password:-[/yellow]")

    send_OTP=r.randrange(1000,9999)
    expires_at = (datetime.now() + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
    print("[bold green]Your OTP is :- [/bold green]",send_OTP)
    otp_hash = int(console.input("[yellow]Enter OTP: -[/yellow]"))
    

    Db.cursor1.execute(
        "SELECT user_id, name, email,password_hash, role, is_verified,is_active FROM users WHERE email = ? and password_hash = ?",
        (email,password)
    )
    user = Db.cursor1.fetchone()
    if user is None:
        print("[bold red]Invalid email or password![/bold red]")
        return None

    user_id, name, email, password_hash, role, is_verified, is_active = user

    if not is_active:
        print("[bold red]Your account is inactive![/bold red]")
        return None

    #for OTP Verification 
    if password != password_hash:
        print("[red]Invalid email or password![/red]")
        return None

    
    
    if send_OTP == otp_hash :
        Db.cursor1.execute("INSERT INTO otp_verification (user_id, otp_hash, expires_at, is_used) VALUES (?, ?, ?, 1)",(user_id, otp_hash,expires_at))
        Db.conn.commit()
        print("[bold green]OTP verified and record inserted![/bold green]")

    else:
        print("[red]Invalid OTP!...[/red]")
        return None
        

    return {
        "user_id": user_id,
        "name": name,
        "email": email,
        "role": role
    }

