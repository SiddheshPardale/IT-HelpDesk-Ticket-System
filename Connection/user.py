from Connection import ConfigureDB as Db
from pathlib import Path
from rich.console import Console
from rich import print
console = Console()


Db.cursor1.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,

    role TEXT NOT NULL DEFAULT 'EMPLOYEE'
        CHECK (role IN ('EMPLOYEE', 'TECHNICIAN', 'ADMIN')),

    is_verified INTEGER NOT NULL DEFAULT 0
        CHECK (is_verified IN (0, 1)),

    specialization TEXT,

    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    photo BLOB,

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);""")
print("Table Created....")

#-------------------------------------
#inserting the data 

# id =int(input("Enter the Id:-"))
# name = input("Enter the name:-")
# email = input("Enter the Email:-")
# password_hash = input("Enter the Password:-")
# role = input("Enter the role:-")
# is_verified = int(input("Enter the is_verified:-"))
# specialization = input("Enter the specialization:-")
# is_active = int(input("Enter the is_active:-"))
# photo = input("Enter the Photo Url:-")
# created_at = input("Enter the created_at :-")
# with open(photo,"rb") as f:
#     file_data = f.read()
# Db.cursor1.execute("insert into users values(?,?,?,?,?,?,?,?,?,?)",(id,name,email,password_hash,role,is_verified,specialization,is_active,file_data,created_at))
# Db.conn.commit()
# print("Inserted The data ")



#-------------------------------------
# #Viwing the data 

# fileid = int(input("Enter the File Id :-"))
# Db.cursor1.execute("select * from users where user_id= ?",(fileid,))
# row=Db.cursor1.fetchone()
# with open("Downloaded_"+row[2]+".jpeg","wb") as f:
#     f.write(row[8])
# print("Img Downloaded.....")


# Note :- to add the image need to give the path without :- " " like- c://photo for above 



def RegisterUser():
    print("\n[bold cyan]========== USER REGISTRATION ==========[/bold cyan]")

    name = console.input("[yellow]Enter Name:-[/yellow] ").strip()
    email = console.input("[yellow]Enter Email:-[/yellow]").strip().lower()
    password = console.input("[yellow]Enter Password:-[/yellow]")

    if not name or not email or not password:
        print("[bold red]Name, email and password are required![/bold red]")
        return

    # Check whether email already exists
    Db.cursor1.execute(
        "SELECT user_id FROM users WHERE email = ?",
        (email,)
    )

    if Db.cursor1.fetchone():
        print("[bold blue]Email already registered![/bold blue]")
        return

    # Hash password before storing it
    # password_hash = bcrypt.hashpw(
    #     password.encode("utf-8"),
    #     bcrypt.gensalt()
    # ).decode("utf-8")

    photo = None
    photo_path = console.input(
        "[yellow]Enter photo path (or press Enter to skip):-[/yellow]"
    ).strip().strip('"')

    if photo_path:
        path = Path(photo_path)

        if not path.is_file():
            print("[bold red]Photo file not found![/bold red]")
            return

        photo = path.read_bytes()

    # Public registration must not allow ADMIN or TECHNICIAN roles
    Db.cursor1.execute("""
        INSERT INTO users
            (name, email, password_hash, role, photo)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, password, "EMPLOYEE", photo))

    Db.conn.commit()
    # Db.conn.close()
    print("[bold green]Registration successful![/bold green]")
    print("[bold green]User ID:-[/bold green]", Db.cursor1.lastrowid)
    print("[bold green]Role: EMPLOYEE[/bold green]")


if __name__ == "__main__":
    try:
        RegisterUser()
    except Exception as error:
        Db.conn.rollback()
        print("[red]Registration failed:[/red]", error)
    finally:
        Db.conn.close()

